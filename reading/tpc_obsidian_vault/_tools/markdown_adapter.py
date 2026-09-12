"""Pandoc-AST adapter for Obsidian; math and source text remain auditable."""
from __future__ import annotations
import copy
import hashlib
import json
import re
import subprocess
from converter_extensions import normalize_math_newlines

READER = 'markdown+tex_math_dollars+tex_math_single_backslash+raw_tex+raw_html+raw_attribute+header_attributes+bracketed_spans+fenced_divs'
# Obsidian uses dollar delimiters. In writer output, escaped square brackets
# such as citation labels are prose, never legacy \\[...\\] math delimiters.
OUTPUT_READER = READER.replace('+tex_math_single_backslash', '-tex_math_single_backslash')
WRITER = ('markdown+tex_math_dollars+pipe_tables+raw_html-raw_attribute-header_attributes'
          '-fenced_divs-bracketed_spans-simple_tables-multiline_tables-grid_tables-smart')

def pandoc(data, source=READER, target='json'):
    result = subprocess.run(['pandoc', '-f', source, '-t', target, '--wrap=none', '--atx-headers'],
                            input=data, text=True, capture_output=True, check=True)
    return result.stdout, result.stderr

def walk(value, kind=None):
    if isinstance(value, dict):
        if 't' in value and (kind is None or value['t'] == kind):
            yield value
        for child in value.values():
            yield from walk(child, kind)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child, kind)

def plain_inlines(value):
    if isinstance(value, dict):
        kind = value.get('t')
        if kind == 'Str': return value['c']
        if kind in ('Space', 'SoftBreak', 'LineBreak'): return ' '
        if kind == 'Math': return '$' + value['c'][1] + '$'
        if kind == 'Code': return value['c'][1]
        if kind in ('Link', 'Image'): return plain_inlines(value['c'][1])
        if kind == 'Span': return plain_inlines(value['c'][1])
        return plain_inlines(value.get('c', []))
    if isinstance(value, list): return ''.join(plain_inlines(v) for v in value)
    return ''

def math_sig(blocks):
    return [(n['c'][0]['t'], re.sub(r'\s+', '', n['c'][1])) for n in walk(blocks, 'Math')]

def anchor(label):
    return 'ref-' + hashlib.sha256(label.encode()).hexdigest()[:16]

def link_node(text, target):
    return {'t':'Link', 'c':[['', [], []], [{'t':'Str','c':text}], [target, '']]}

def adapt(markdown, *, origin, destination, owner, mapper, citation, source_reader=READER):
    raw, warnings = pandoc(markdown,source_reader)
    ast = json.loads(raw)
    blocks = ast['blocks']
    initial_math = math_sig(blocks)
    title_math_nodes=len(list(walk(blocks[0],'Math'))) if blocks and blocks[0]['t']=='Header' and blocks[0]['c'][0]==1 else 0
    labels = {}
    heading_targets = {}
    used_anchors = set()
    # Establish a visible, stable anchor for source labels. This does not
    # reconstruct or claim printed theorem/equation numbering.
    for node in walk(blocks, 'Header'):
        attrs = node['c'][1]
        title = plain_inlines(node['c'][2]).strip()
        if attrs[0]: heading_targets[attrs[0]] = title
    expanded = []
    for block in blocks:
        discovered = []
        for node in walk(block):
            if node['t'] in ('Span', 'Image'):
                if node['c'][0][0]: discovered.append(node['c'][0][0])
            elif node['t'] == 'Math':
                discovered.extend(re.findall(r'\\label\{([^}]+)\}', node['c'][1]))
            elif node['t'] in ('RawInline', 'RawBlock') and node['c'][0] == 'html':
                discovered.extend(re.findall(r'\bid=["\']([^"\']+)["\']', node['c'][1]))
        for label in discovered:
            name = anchor(label)
            labels[label] = name
            if name not in used_anchors:
                expanded.append({'t':'Header','c':[6, ['', [], []], [{'t':'Str','c':name}]]})
                used_anchors.add(name)
        expanded.append(block)
    blocks = expanded
    adaptations = dict(source_label_anchors=len(labels), citation_links=0,
                       normalized_math_linebreaks=0, label_commands_retained=0)
    for node in list(walk(blocks)):
        kind = node['t']
        if kind == 'Math':
            if '\n' in node['c'][1] or '\r' in node['c'][1]:
                adaptations['normalized_math_linebreaks'] += 1
                node['c'][1] = normalize_math_newlines(node['c'][1],display=node['c'][0]['t']=='DisplayMath')
            # Label commands remain in mathematical source. MathJax checking
            # below uses a fresh TeX state per expression to avoid false
            # cross-document duplicate-label reports.
            adaptations['label_commands_retained'] += len(re.findall(r'\\label\{', node['c'][1]))
        elif kind in ('Link', 'Image'):
            target = node['c'][-1][0]
            node['c'][-1][0] = mapper(target, origin, destination, owner, labels, heading_targets)
            node['c'][0] = ['', [], []]
        elif kind == 'Code' and re.fullmatch(r'\\cite\w*\s*(?:\[[^]]*\]\s*){0,2}\{[^}]+\}', node['c'][1]):
            raw_cite = node['c'][1]
            keys = raw_cite[raw_cite.rfind('{')+1:-1].split(',')
            inlines = []
            for i, key in enumerate(keys):
                if i: inlines.append({'t':'Str','c':'; '})
                key = key.strip()
                linked=link_node('['+key+']',citation(owner,key,destination,raw_cite))
                if i==0:
                    linked['c'][1]=[{'t':'Code','c':[['',[],[]],raw_cite]}]
                inlines.append(linked)
            node.clear(); node.update(t='Span', c=[['', [], []], inlines])
            adaptations['citation_links'] += len(keys)
        elif kind == 'Cite':
            inlines = []
            visible=copy.deepcopy(node['c'][1])
            for i, item in enumerate(node['c'][0]):
                if i: inlines.append({'t':'Str','c':'; '})
                key = item['citationId']
                linked=link_node('['+key+']',citation(owner,key,destination,
                                 'Pandoc citation metadata: '+json.dumps(item,ensure_ascii=False,sort_keys=True)))
                if i==0:linked['c'][1]=visible
                inlines.append(linked)
            node.clear(); node.update(t='Span', c=[['', [], []], inlines])
            adaptations['citation_links'] += len(inlines)
        elif kind == 'Header':
            node['c'][1] = ['', [], []]
        elif kind == 'Span':
            node['c'][0] = ['', [], []]
        elif kind in ('RawInline', 'RawBlock') and node['c'][0] == 'html':
            if re.fullmatch(r'\s*</?span\b[^>]*>\s*', node['c'][1]):
                node['c'][1] = ''
    out_ast = dict(ast, meta={}, blocks=blocks)
    writer_ast=copy.deepcopy(out_ast)
    for node in list(walk(writer_ast['blocks'],'CodeBlock')):
        attrs,literal=node['c']
        # Pandoc 2.x strips leading blank lines even for fenced CodeBlock
        # output. Emit an explicit safe-length fence, then demand that its
        # re-parsed literal text is exactly the original AST text.
        fence='`'*max(3,1+max((len(m[0]) for m in re.finditer(r'`+',literal)),default=0))
        language=attrs[1][0] if attrs[1] and re.fullmatch(r'[A-Za-z0-9_-]+',attrs[1][0]) else 'text'
        node.clear();node.update(t='RawBlock',c=['markdown',fence+language+'\n'+literal+'\n'+fence])
    output, write_warnings = pandoc(json.dumps(writer_ast, ensure_ascii=False), 'json', WRITER)
    recovered = json.loads(pandoc(output, OUTPUT_READER)[0])
    after_math = math_sig(recovered['blocks'])
    expected = math_sig(blocks)
    if initial_math != expected:
        raise ValueError(f'Adapter changed math content before export: {owner}')
    if expected != after_math:
        raise ValueError(f'Obsidian Markdown math roundtrip mismatch: {owner}, {len(expected)} vs {len(after_math)}')
    # Compare transformed AST prose against the re-parsed reading layer.
    expected_plain = pandoc(json.dumps(out_ast, ensure_ascii=False), 'json', 'plain')[0]
    recovered_plain = pandoc(json.dumps(recovered, ensure_ascii=False), 'json', 'plain')[0]
    def prose_signature(text):
        # The plain writer draws table border lines according to AST column
        # widths. Markdown changes those widths without changing cell text.
        text=re.sub(r'(?m)^[ \t]*[-:]{3,}[-: \t]*$','',text)
        return re.sub(r'\s+','',text)
    text_equal = prose_signature(expected_plain) == prose_signature(recovered_plain)
    def literal_signature(value):
        return [(n['t'],n['c'][1]) for n in walk(value) if n['t'] in ('Code','CodeBlock')]
    literal_equal=literal_signature(blocks)==literal_signature(recovered['blocks'])
    if not literal_equal:raise ValueError('Literal code changed in Markdown roundtrip: '+owner)
    report = dict(owner=owner, origin=str(origin), destination=destination, source_reader=source_reader,
                  math_nodes=len(expected), title_math_nodes=title_math_nodes, math_sequence_sha256=hashlib.sha256(
                      json.dumps(expected, ensure_ascii=False).encode()).hexdigest(),
                  math_roundtrip=True, text_roundtrip=text_equal, literal_code_roundtrip=literal_equal,
                  heading_targets=heading_targets, label_targets=labels,
                  warnings=(warnings + write_warnings).strip(), **adaptations)
    formulas = [dict(kind=node['c'][0]['t'], tex=node['c'][1]) for node in walk(blocks,'Math')]
    return output, report, formulas
