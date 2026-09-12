"""Bounded, vault-local reader fixes; never modify the archived converter.

1. Balanced literal verbatim blocks without input commands are inert content.
2. Newlines inside a Math AST node are whitespace, not Markdown hard breaks.
3. Source-backed standalone star math is grouped to avoid a reader defect;
   any remaining empty Math node blocks conversion.
4. TeX comments within a multi-target cref are whitespace, not label names.
"""
import re

NOTICE = ('Vault-local reader extensions v3: inline verb commands are conservatively rejected; standalone uncommented inert verbatim '
          'is protected through environment preprocessing; comment-free math-node '
          'line endings are normalized to spaces; literal source \\(*\\) is grouped '
          'as \\({*}\\) to preserve its star through the Pandoc reader; remaining '
          'empty math nodes are rejected. Canonically shaped multi-label references '
          'may have TeX comments removed, without joining whitespace inside a label. '
          'Original source bytes are unchanged. '
          'No TeX execution, source repair, or mathematical certification.')

def verbatim_spans(raw):
    """Accept only explicit, uncommented delimiter lines, with bounded content."""
    starts = re.compile(r'^[ \t]*\\begin\{verbatim\}[ \t]*(?:\r?\n)?$')
    ends = re.compile(r'^[ \t]*\\end\{verbatim\}[ \t]*(?:\r?\n)?$')
    spans=[]; start=None; offset=0
    for line in raw.splitlines(keepends=True):
        has_open=r'\begin{verbatim}' in line
        has_end=r'\end{verbatim}' in line
        if has_open:
            if start is not None or not starts.fullmatch(line):
                raise ValueError('Nested, commented, or non-standalone verbatim delimiter')
            start=offset
        elif has_end:
            if start is None or not ends.fullmatch(line):
                raise ValueError('Unbalanced, commented, or non-standalone verbatim delimiter')
            end=offset+len(line)
            block=raw[start:end]
            if re.search(r'\\(?:input|include|addbibresource|bibliography)\b|\\(?:begin|end)\{(?:document|thebibliography)\}',block):
                raise ValueError('Parser-sensitive literal command in verbatim requires explicit handling')
            spans.append((start,end)); start=None
        offset+=len(line)
    if start is not None:
        raise ValueError('Unclosed verbatim environment')
    return spans

def mask_verbatim(raw):
    result=list(raw)
    for start,end in verbatim_spans(raw):
        result[start:end]=['\n' if c=='\n' else ' ' for c in raw[start:end]]
    return ''.join(result)

def normalize_math_newlines(text, *, display=False):
    comment=re.search(r'(?<!\\)(?:\\\\)*%',text)
    if display and comment:
        return text  # Display math can retain TeX comment line boundaries.
    if ('\n' in text or '\r' in text) and comment:
        raise ValueError('Comment-sensitive math newline requires source-backed handling')
    return text.replace('\r',' ').replace('\n',' ')

def install(converter):
    import source_markdown_includes as includes
    strict = includes.require_static_input_context
    def inert_context(raw):
        strict(mask_verbatim(raw))
    includes.require_static_input_context = inert_context
    converter.require_static_input_context = inert_context
    old_environments=converter.preserve_environments
    def environments(raw):
        parts=[]; catalog=[]; cursor=0
        spans=verbatim_spans(raw)+[(len(raw),len(raw))]
        for start,end in spans:
            piece=raw[cursor:start]
            if re.search(r'\\verb(?:\*|(?=[^A-Za-z]))',piece):
                raise ValueError('Inline verbatim requires explicit preservation; conversion refused')
            # The source token is genuinely nonempty. Grouping retains the
            # exact star glyph instead of trusting the reader's empty node.
            piece=piece.replace(r'\(*\)',r'\({*}\)')
            converted,items=old_environments(piece)
            for item in items:
                item['line']+=raw.count('\n',0,cursor)
            catalog.extend(items); parts.extend([converted,raw[start:end]])
            cursor=end
        return ''.join(parts),catalog
    converter.preserve_environments=environments
    old_headings=converter.headings
    old_displays=converter.display_blocks
    converter.headings=lambda raw: old_headings(mask_verbatim(raw))
    # Catalog raw display bytes outside verbatim without counting literals.
    def displays(raw):
        hidden=verbatim_spans(raw)
        lines={raw.count('\n',0,s)+1 for s,e in hidden}
        for item in old_displays(raw):
            offset=sum(len(s) for s in raw.splitlines(keepends=True)[:item['start']-1])
            if not any(s<=offset<e for s,e in hidden):
                yield item
    converter.display_blocks=displays
    old_separate = converter.separate_math_from_digits
    def spacing(value):
        for node in list(converter.nodes(value, 'Math')):
            if not node['c'][1].strip():
                raise ValueError('Empty reader Math node: source token must be audited, not assumed empty')
            else:
                node['c'][1] = normalize_math_newlines(node['c'][1],display=node['c'][0]['t']=='DisplayMath')
        return old_separate(value)
    converter.separate_math_from_digits = spacing
    old_remap = converter.remap_links
    def remap(blocks, *args, **kwargs):
        for node in converter.nodes(blocks, 'Link'):
            target = node['c'][-1][0]
            attrs = dict(node['c'][0][2])
            if (target.startswith('#') and ',' in target and '%' in target
                    and attrs.get('reference') == target[1:]
                    and attrs.get('reference-type') == 'ref'):
                reference=target[1:]
                if (set(node)!={'t','c'} or node['c'][0] != ['',[],[['reference-type','ref'],['reference',reference]]]
                        or node['c'][1] != [{'t':'Str','c':'['+reference+']'}]
                        or node['c'][-1] != [target,'']):
                    raise ValueError('Noncanonical commented reference: preserve custom visible text and attributes')
                cleaned = re.sub(r'%[^\n]*(?:\n|$)', '', target[1:])
                cleaned = ','.join(piece.strip() for piece in cleaned.split(','))
                if not re.fullmatch(r'[^,\s%]+(?:,[^,\s%]+)+', cleaned):
                    raise ValueError('Unsupported commented multi-label reference')
                node['c'][0] = ['', [], [['reference-type', 'ref'], ['reference', cleaned]]]
                node['c'][1] = [{'t':'Str', 'c':'[' + cleaned + ']'}]
                node['c'][-1][0] = '#' + cleaned
        args=list(args)
        # tex is the second positional argument after paper, or a keyword.
        if len(args)>=2: args[1]=mask_verbatim(args[1])
        elif 'tex' in kwargs: kwargs['tex']=mask_verbatim(kwargs['tex'])
        return old_remap(blocks, *args, **kwargs)
    converter.remap_links = remap
