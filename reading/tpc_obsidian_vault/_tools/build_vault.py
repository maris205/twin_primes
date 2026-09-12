#!/usr/bin/env python3
"""Build a portable, source-locked Obsidian reading and navigation layer.

Only generated files inside this vault are writable. Hand-edited generated
files cause a conflict, and 80_我的笔记 plus existing Obsidian settings are never
overwritten. Source code and archived Markdown are never executed.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import threading
from urllib.parse import quote, unquote, urlsplit

from prepare_sources import VAULT, CACHE, DEFAULT_SOURCE, PREPARER_VERSION, digest, source_snapshot, cache_integrity, require_cache_payload
from markdown_adapter import adapt, anchor, READER, OUTPUT_READER

DATE = '2026-09-12'
VERSION = 'tpc-obsidian-v1'
SUMMARY = 'synthesis/seven-island-monograph/'
PHYSICAL = 'research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/'
ISLANDS = {
    '1':('岛01-基础算术', '基础算术：局部筛、相关和与物理计数'),
    '2':('岛02-解析消去', '解析消去：完整系数下的有符号集体估计'),
    '3':('岛03-固定原子', '固定原子：物理移位2与带掩码拉回'),
    '4':('岛04-实际出现项', '实际出现项：Pair-native与H1结构'),
    '5':('岛05-非自治动力学', '非自治动力学：移动靶与指定算术种子'),
    '6':('岛06-孪生素数终点', '孪生素数终点：无穷多个素数对'),
    '7':('岛07-几何辅助提升', '几何辅助提升：Hénon与精确附接'),
}

def short_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()[:16]

def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'

def properties(**values):
    return '---\n' + '\n'.join(k+': '+json.dumps(v, ensure_ascii=False) for k,v in values.items()) + '\n---\n\n'

def wiki(path, label=None):
    target = str(path).removesuffix('.md')
    return '[[' + target + ('|' + label if label else '') + ']]'

def relative_link(target, source, fragment=''):
    path = os.path.relpath(str(target), str(Path(source).parent))
    return quote(path, safe='/.-_') + ('#' + quote(fragment, safe='-_.') if fragment else '')

def sanitize(text):
    return re.sub(r'[^A-Za-z0-9._-]+', '-', text).strip('-') or short_hash(text)

def bib_entries(text):
    """Retain balanced entries verbatim; do not manufacture formatted metadata."""
    entries = []
    pos = 0
    token = re.compile(r'@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,')
    while match := token.search(text, pos):
        start = match.start()
        i = text.index('{', start)
        depth = 0
        while i < len(text):
            if text[i] == '{' and (i == 0 or text[i-1] != '\\'): depth += 1
            elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
                depth -= 1
                if depth == 0:
                    entries.append((match[2], text[start:i+1]))
                    pos = i+1
                    break
            i += 1
        else:
            raise ValueError('Unbalanced source bibliography entry: '+match[2])
    return entries

class VaultBuilder:
    def __init__(self, source):
        self.source = source.resolve()
        self.baseline = json.loads((CACHE / 'source_baseline.json').read_text())
        if source_snapshot(self.source) != self.baseline['files']:
            raise ValueError('Source changed since preparation')
        self.inventory = json.loads((CACHE/'inventory.json').read_text())
        self.rows = [json.loads((CACHE/'papers'/(row['id']+'.json')).read_text()) for row in self.inventory]
        fingerprint=hashlib.sha256(('\n'.join(digest(p) for p in [
            Path(__file__).with_name('prepare_sources.py'),Path(__file__).with_name('converter_extensions.py'),
            self.source/'research/tpc-big-road/maintain_source_markdown.py',
            self.source/'research/tpc-big-road/source_markdown_includes.py'])).encode()).hexdigest()
        for original,cached in zip(self.inventory,self.rows):
            if (not all(cached.get(k)==v for k,v in original.items())
                    or cached.get('source_head')!=self.baseline['repository_head']
                    or cached.get('preparer_version')!=PREPARER_VERSION
                    or cached.get('reader_fingerprint')!=fingerprint
                    or cached.get('content_integrity')!=cache_integrity(cached)):
                raise ValueError('Stale or damaged preparation cache: '+original['id'])
            require_cache_payload(cached)
        self.by_id = {row['id']:row for row in self.rows}
        self.by_directory = {row['directory']:row for row in self.rows}
        self.by_number = defaultdict(list)
        for row in self.rows: self.by_number[row['number']].append(row)
        self.old_path = VAULT/'99_维护/generated_manifest.json'
        self.previous = json.loads(self.old_path.read_text()).get('files', {}) if self.old_path.exists() else {}
        self.generated = {}
        self.origins = {}
        self.note_sources = {}
        self.queue = deque()
        self.queued = set()
        self.processed = set()
        self.adapt_reports = []
        self.formulas = []
        self.edges = []
        self.link_rewrites = []
        self.unresolved = {}
        self.locators = defaultdict(dict)
        self.citations = defaultdict(dict)
        self.bibliographies = defaultdict(lambda: defaultdict(list))
        self.mentions = defaultdict(dict)
        self.source_copies = {}

    def put(self, relative, content):
        rel = Path(relative)
        if rel.is_absolute() or '..' in rel.parts or rel.parts[0] in ('80_我的笔记', '_tools', '.build', '.obsidian'):
            raise ValueError('Not a generated output target: '+str(relative))
        path = VAULT/rel
        if path.resolve() != path.absolute() or not path.resolve().is_relative_to(VAULT):
            raise ValueError('Symlinked/rebound output target')
        data = content.encode() if isinstance(content, str) else content
        wanted = hashlib.sha256(data).hexdigest()
        if path.exists():
            current = digest(path)
            known=self.generated.get(str(rel),self.previous.get(str(rel)))
            if current != wanted and known != current:
                raise ValueError('Refusing to overwrite hand-edited/unrecognized file: '+str(rel))
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or digest(path) != wanted:
            path.write_bytes(data)
        self.generated[str(rel)] = wanted
        return str(rel)

    def attachment(self, source_path):
        path = Path(source_path)
        rel = str(path.relative_to(self.source))
        if rel in self.source_copies: return self.source_copies[rel]['vault_path']
        if rel not in self.baseline['files']:
            raise ValueError('Attachment not in preserved source baseline: '+rel)
        suffix = '.txt' if path.suffix.lower() in ('.md', '.py', '.sh', '.json', '.yaml', '.yml') else ''
        target = '90_附件/原始资料/' + rel + suffix
        self.put(target, path.read_bytes())
        self.source_copies[rel] = dict(vault_path=target, sha256=digest(path), original_path=rel)
        return target

    def allowed(self, path):
        if not path.is_relative_to(self.source): return False
        relative = str(path.relative_to(self.source))
        if relative.startswith('papers/'):
            return len(path.relative_to(self.source).parts)>1 and path.relative_to(self.source).parts[1] in self.by_directory
        return (relative.startswith(('research/tpc-big-road/', SUMMARY))
                or len(path.relative_to(self.source).parts) == 1 and path.suffix == '.md')

    def queue_note(self, origin, target=None, owner=None, banner=None, markdown=None):
        origin = Path(origin)
        rel = str(origin.relative_to(self.source))
        if rel in self.origins:
            return self.origins[rel]
        if target is None:
            parts = origin.relative_to(self.source).parts
            if parts[0] == 'papers' and parts[1] in self.by_directory:
                row = self.by_directory[parts[1]]
                owner = row['id']
                tail = '--'.join(parts[2:]).removesuffix('.md')
                target = '06_研究资料/论文补充/' + owner + '--' + sanitize(tail) + '.md'
            else:
                owner = owner or 'DOC-' + short_hash(rel)
                target = '06_研究资料/历史与证明/' + sanitize(origin.stem) + '--' + short_hash(rel)[:8] + '.md'
        owner = owner or 'DOC-' + short_hash(rel)
        self.origins[rel] = target
        self.note_sources[target] = rel
        if target not in self.queued:
            self.queue.append(dict(origin=origin, target=target, owner=owner, banner=banner, markdown=markdown))
            self.queued.add(target)
        return target

    def source_location(self, path, line, owner, destination):
        # A live Obsidian heading replaces a nonfunctional TeX #L fragment.
        rel = str(path.relative_to(self.source))
        key = rel + ':' + str(line)
        heading = 'src-' + short_hash(key)
        self.locators[owner][heading] = dict(path=rel, line=line)
        return relative_link('99_维护/源定位/'+owner+'.md', destination, heading)

    def missing(self, target, origin, destination, reason):
        key = str(origin.relative_to(self.source)) + '|' + target + '|' + reason
        ident = 'issue-' + short_hash(key)
        self.unresolved[ident] = dict(target=target, source=str(origin.relative_to(self.source)),
                                     destination=destination, reason=reason)
        return relative_link('99_维护/待解决来源链接.md', destination, ident)

    def map_link(self, target, origin, destination, owner, labels, headings):
        original_target = target
        if not target:
            return self.missing(target, origin, destination, 'Empty link target in preserved source')
        if target.startswith(('http://', 'https://', 'mailto:', 'doi:')):
            return target
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            return self.missing(target, origin, destination, 'Unsupported source URI; retained as text in issue record')
        path_part, sep, fragment = unquote(target).partition('#')
        # Old absolute links are relocated only by an existing, in-scope
        # standalone relative path; no old-repository file is accessed.
        legacy_prefix = '/root/autodl-tmp/math_research3/prime_dynamics_theory/'
        if path_part.startswith(legacy_prefix):
            path_part = str(self.source / path_part[len(legacy_prefix):])
        # Markdown source links sometimes encode editor-style :line suffixes.
        if match := re.match(r'^(.*\.(?:md|tex|py)):(\d+)$', path_part):
            path_part, fragment = match[1], 'L'+match[2]
        path = (origin.parent/path_part).resolve() if path_part else origin
        if not self.allowed(path):
            return self.missing(original_target, origin, destination, 'Outside the standalone TPC source scope')
        rel = str(path.relative_to(self.source))
        if path_part == '' and fragment:
            if fragment in labels:
                result = relative_link(destination, destination, labels[fragment])
            elif fragment in headings:
                result = relative_link(destination, destination, headings[fragment])
            else:
                # Check original TeX labels for summaries and non-AST anchors.
                result = self.missing(original_target, origin, destination, 'Source anchor has no parsed heading or label')
            return result
        if not path.exists():
            if rel in self.origins:
                return relative_link(self.origins[rel], destination)
            return self.missing(original_target, origin, destination, 'Source path is unavailable; no substitute invented')
        if path.is_symlink() or path.resolve() != path.absolute():
            return self.missing(original_target, origin, destination, 'Symlinked/rebound source not imported')
        if path.is_dir():
            if path.parent == self.source/'papers' and path.name in self.by_directory:
                result = relative_link('02_论文/'+self.by_directory[path.name]['id']+'.md', destination)
            elif (path/'README.md').is_file():
                result = relative_link(self.queue_note(path/'README.md'), destination)
            else:
                return self.missing(original_target, origin, destination, 'Directory has no selected reading entry')
        elif fragment.startswith('L') and fragment[1:].isdigit():
            line = int(fragment[1:])
            content = path.read_text(errors='replace').splitlines()
            if 1 <= line <= len(content):
                nearby = re.findall(r'\\label\{([^}]+)\}', content[line-1])
                matched = next((key for key in nearby if key in labels), None)
                result = relative_link(destination, destination, labels[matched]) if matched else self.source_location(path, line, owner, destination)
            else:
                return self.missing(original_target, origin, destination, 'Source line is out of range')
        elif path.suffix.lower() == '.md':
            mapped = self.origins.get(rel) or self.queue_note(path)
            # Cross-document source anchors are resolved after every note is
            # parsed, using a deferred map (not guessed slug equality).
            result = relative_link(mapped, destination)
            if fragment:
                result += '#pending-' + quote(fragment, safe='-_.')
        else:
            result = relative_link(self.attachment(path), destination, fragment if path.suffix.lower() == '.pdf' else '')
        if result != original_target:
            self.link_rewrites.append(dict(note=destination, original=original_target, rewritten=result,
                                           resolved_source=rel))
        return result

    def cite(self, owner, key, destination, raw):
        self.citations[owner].setdefault(key, dict(raw_commands=set(), citing_notes=set()))
        self.citations[owner][key]['raw_commands'].add(raw)
        self.citations[owner][key]['citing_notes'].add(destination)
        return relative_link('99_维护/参考文献/'+owner+'.md', destination, 'cite-'+short_hash(key))

    def collect_bib(self, owner, directory):
        for path in sorted(directory.rglob('*.bib')):
            if path.is_symlink(): continue
            self.attachment(path)
            for key, entry in bib_entries(path.read_text()):
                self.bibliographies[owner][key].append(dict(source=str(path.relative_to(self.source)), raw=entry))
        # Inline thebibliography entries are retained if no external entry has
        # the key. Citation-to-paper relations are still mere source references.
        for path in sorted(directory.rglob('*.tex')):
            text = path.read_text(errors='replace')
            matches = list(re.finditer(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', text))
            for i, match in enumerate(matches):
                end = matches[i+1].start() if i+1<len(matches) else text.find(r'\end{thebibliography}', match.end())
                if end == -1: continue
                self.bibliographies[owner][match[1]].append(dict(source=str(path.relative_to(self.source)),raw=text[match.start():end].strip()))

    def extract_mentions(self, row):
        directory = self.source/'papers'/row['directory']
        for path in sorted(directory.rglob('*.tex')):
            for line_no, line in enumerate(path.read_text(errors='replace').splitlines(), 1):
                for hit in re.finditer(r'(?i)(?:\bTPC[-\s]*|WangTPC)(\d{1,3})(?!\d)', line):
                    number = int(hit[1])
                    if number == row['number'] or number not in self.by_number: continue
                    if number not in self.mentions[row['id']]:
                        self.mentions[row['id']][number] = dict(path=str(path.relative_to(self.source)), line=line_no, excerpt=line.strip())

    def register_sources(self):
        for row in self.rows:
            owner = row['id']
            directory = self.source/'papers'/row['directory']
            if row['conversion_status'] == 'SOURCE_UNAVAILABLE': continue
            if row['conversion_status'] == 'CONVERSION_BLOCKED':
                raise ValueError('Unresolved full-source conversion: '+owner)
            origin = self.source/row['reading_source_path']
            self.queue_note(origin, '03_全文/'+owner+'.md', owner,
                '原文阅读层；转换状态不等于定理认证。公式与印刷编号以原 PDF/TeX 为准。', row['markdown'])
            self.collect_bib(owner, directory)
            self.extract_mentions(row)
            for path in sorted(directory.rglob('*.tex')):
                self.attachment(path)
            self.attachment(self.source/row['paths']['pdf'])
            for name in ['README.md', 'PROOF_PACKAGE.md', 'DERIVATION_PACKAGE.md', 'APPLICATIONS.md', 'APPLICABILITY.md', 'CLAIM_BOUNDARY.md']:
                path = directory/name
                if path.is_file(): self.queue_note(path)
            # New records are derived vault artifacts, never written to papers/.
            self.queue_note(directory/'CONVERSION_RECORD.md', '99_维护/转换记录/'+owner+'.md', owner,
                '转换记录快照。原记录中的路径与 SHA-256 指原仓库，不指适配后的知识库文件。', row['record'])
        special = [
            (SUMMARY+'paper/main.md', '05_综合与进展/七岛综合稿-中文.md', 'SYNTHESIS-ZH', '2026-09-12 中文综合稿，保留完整正文。文档组织不构成新的数学结果。'),
            (SUMMARY+'paper-en/main.md', '05_综合与进展/七岛综合稿-English.md', 'SYNTHESIS-EN', '2026-09-12 English synthesis; full translation, not a new mathematical result.'),
            ('research/tpc-big-road/TPC_HISTORY_SUMMARY.md', '05_综合与进展/研究历史总结-原文.md', 'HISTORY', '历史总结原文。关于“当前”“最强结果”及旧混合仓库范围的表述按原日期理解，参见历史总结校注与当前状态。'),
            ('research/tpc-big-road/TPC_ROUTE_MAP.md', '05_综合与进展/历史路线图-原文.md', 'ROUTE-HISTORY', '历史路线原文，包含不同日期的 YOU ARE HERE 和 DONE 标记。它们不是今天的研究状态或继续研究授权。'),
            ('research/tpc-big-road/TPC_ISLAND_MAP_GUIDE.md', '05_综合与进展/七岛地图说明-原文.md', 'MAP-GUIDE', '稳定的七岛和两桥含义；当前状态另见交接快照。'),
            ('TPC_HANDOFF.md', '05_综合与进展/交接文档-完整快照.md', 'HANDOFF', '生成时的完整交接快照。头部与其指定入口决定当时状态；旧段落中的指令与状态按历史记录阅读。'),
            (PHYSICAL+'README.md', '05_综合与进展/实际算子研究汇总-2026-09-09.md', 'PHYSICAL-SUMMARY', '未编号实际算子研究总结；正式编号终点仍为 TPC418，全文有符号节省尚未证明。'),
            ('research/tpc-big-road/PAPER_CANDIDATE_LEDGER.md', '05_综合与进展/历史论文候选账本.md', 'PAPER-LEDGER', '历史论文逐项记录；候选、条件和停止状态原样保留，不自动提升为定理。'),
        ]
        for rel, target, owner, banner in special:
            path = self.source/rel
            if path.is_file(): self.queue_note(path,target,owner,banner)
        for lang, owner in [('paper','SYNTHESIS-ZH'),('paper-en','SYNTHESIS-EN')]:
            self.collect_bib(owner, self.source/SUMMARY/lang)
        matrix = json.loads((self.source/SUMMARY/'CORE_SOURCE_MATRIX.json').read_text())
        for item in matrix['sources']:
            path = self.source/item['path']
            if path.suffix == '.md': self.queue_note(path)
        for path in sorted((self.source/PHYSICAL).glob('*.md')):
            self.queue_note(path)

    def process_notes(self):
        # Only Pandoc/AST work is parallel. Shared source routing is serialized;
        # final note writes and order remain owned by the main builder thread.
        lock=threading.RLock()
        route_cache={}
        def mapped(*args):
            key=tuple(str(v) for v in args[:4])
            with lock:
                if key not in route_cache:route_cache[key]=self.map_link(*args)
                return route_cache[key]
        def cited(*args):
            with lock:return self.cite(*args)
        def prepare(item):
            raw=item['markdown'] if item['markdown'] is not None else item['origin'].read_text()
            return adapt(raw,origin=item['origin'],destination=item['target'],owner=item['owner'],
                         mapper=mapped,citation=cited,
                         source_reader=OUTPUT_READER if item['markdown'] is not None or item['origin'].name=='main.md' else READER)
        with ThreadPoolExecutor(max_workers=6) as pool:
            self._process_batches(pool,prepare)

    def _process_batches(self,pool,prepare):
        while self.queue:
            batch=[]
            while self.queue and len(batch)<24:
                item=self.queue.popleft()
                if item['target'] not in self.processed:batch.append(item)
            results=list(pool.map(prepare,batch))
            for item,result in zip(batch,results):
                self._write_processed_note(item,result)

    def _write_processed_note(self,item,result):
            origin, target, owner = item['origin'], item['target'], item['owner']
            markdown, report, formulas = result
            if target.startswith('03_全文/'):
                source_record=self.by_id[owner]['record']
                counted=re.search(r'Pandoc math-node sequence: `(\d+)` before writing and `(\d+)` after Markdown parsing',source_record)
                if counted is None or report['math_nodes']-report['title_math_nodes']!=int(counted[2]):
                    raise ValueError('Reading-layer math count differs from source conversion record: '+owner)
            intro = properties(type='source-reading', source_path=str(origin.relative_to(self.source)),
                               snapshot_date=DATE, owner=owner, generated=True,
                               semantic_review='not-certified-by-conversion')
            if item['banner']:
                intro += '> [!info] 阅读范围\n> ' + item['banner'] + '\n\n'
            if owner in self.by_id:
                intro += '论文入口：'+wiki('02_论文/'+owner+'.md',owner)+' · '+wiki('00_开始阅读.md','首页')+'\n\n'
            else:
                intro += wiki('00_开始阅读.md','首页')+' · '+wiki('05_综合与进展/历史总结校注.md','历史与当前状态的区别')+'\n\n'
            self.put(target, intro+markdown)
            self.adapt_reports.append(report)
            self.formulas.extend(dict(note=target, index=i, **formula) for i,formula in enumerate(formulas,1))
            self.processed.add(target)
            if len(self.processed)%40 == 0:
                print('Adapted',len(self.processed),'notes; queue',len(self.queue),flush=True)

    def write_reference_notes(self):
        for owner, entries in sorted(self.citations.items()):
            target='99_维护/参考文献/'+owner+'.md'
            lines=[properties(type='source-citation-index', owner=owner, generated=True),
                   '# '+owner+' 引用键与原始书目\n',
                   '引用键来自原文；以下内容保留原始书目字段，不是重新检索或核验出版信息。未匹配键明确列出，不补造条目。\n']
            for key, uses in sorted(entries.items()):
                lines += ['## cite-'+short_hash(key)+'\n', '**'+key+'**\n']
                values=self.bibliographies[owner].get(key,[])
                unique={v['raw']:v for v in values}
                if unique:
                    for value in unique.values():
                        lines += ['来源：`'+value['source']+'`\n', '```bibtex\n'+value['raw']+'\n```\n']
                else:
                    lines += ['> [!warning] 未匹配书目键\n> 已保留原始命令，不据引用键臆造作者、题目或结论。\n']
                lines += ['原始引用命令：'+', '.join('`'+v+'`' for v in sorted(uses['raw_commands']))+'\n',
                          '引用处：'+' · '.join(wiki(v,Path(v).stem) for v in sorted(uses['citing_notes']))+'\n']
            self.put(target,'\n'.join(lines))

    def write_locators(self):
        for owner, items in sorted(self.locators.items()):
            lines=[properties(type='source-locator', generated=True), '# '+owner+' 原始源码定位\n',
                   '以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。\n']
            for heading,item in sorted(items.items()):
                path=self.source/item['path']
                content=path.read_text(errors='replace').splitlines()
                start=max(1,item['line']-2); end=min(len(content),item['line']+5)
                excerpt='\n'.join(f'{i}: {content[i-1]}' for i in range(start,end+1))
                self.attachment(path)
                lines += ['## '+heading+'\n', '`'+item['path']+'`，原始第 '+str(item['line'])+' 行。\n',
                          '````text\n'+excerpt+'\n````\n']
            self.put('99_维护/源定位/'+owner+'.md','\n'.join(lines))

    def finalize(self):
        if source_snapshot(self.source) != self.baseline['files']:
            raise ValueError('Source preservation check failed')
        self.put('99_维护/source_manifest.json',json_text(dict(source_head=self.baseline['repository_head'],
                  snapshot_date=DATE, source_files=self.source_copies)))
        self.put('99_维护/adaptation_report.json',json_text(self.adapt_reports))
        self.put('99_维护/relations.json',json_text(self.edges))
        self.put('99_维护/link_rewrites.json',json_text(self.link_rewrites))
        self.put('99_维护/论文清单.json',json_text([{k:v for k,v in row.items() if k not in ('markdown','record','lexical_evidence')}
                                                       for row in self.rows]))
        (CACHE/'math_nodes.json').write_text(json_text(self.formulas))
        stale=sorted(set(self.previous)-set(self.generated))
        # The manifest is self-excluded to avoid a hash recursion.
        self.old_path.parent.mkdir(parents=True,exist_ok=True)
        self.old_path.write_text(json_text(dict(version=VERSION, files=self.generated,
            stale_retained=stale, user_notes_protected=True, source_preserved=True)))
        print(json_text(dict(generated=len(self.generated), notes=len(self.processed),
                             math_nodes=len(self.formulas), unresolved=len(self.unresolved),
                             source_copies=len(self.source_copies))),flush=True)

    def save_incomplete(self):
        self.old_path.parent.mkdir(parents=True,exist_ok=True)
        self.old_path.write_text(json_text(dict(version=VERSION, files={**self.previous,**self.generated},
                                               build_incomplete=True)))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=DEFAULT_SOURCE)
    args=parser.parse_args()
    builder=VaultBuilder(args.source)
    try:
        builder.register_sources()
        builder.process_notes()
        from vault_content import write_content
        write_content(builder)
        builder.process_notes()
        builder.write_reference_notes()
        builder.write_locators()
        from vault_checks import resolve_deferred_links, write_issue_note
        resolve_deferred_links(builder)
        write_issue_note(builder)
        builder.finalize()
    except BaseException:
        builder.save_incomplete()
        raise

if __name__ == '__main__':
    main()
