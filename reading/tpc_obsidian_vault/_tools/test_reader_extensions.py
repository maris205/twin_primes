#!/usr/bin/env python3
"""Regression tests for source-reader hazards found during the vault audit."""
import importlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'twin_primes/research/tpc-big-road'))
import maintain_source_markdown as converter
import source_markdown_includes as includes
import converter_extensions as ext

class ReaderTests(unittest.TestCase):
    def setUp(self):
        importlib.reload(includes); importlib.reload(converter)
        ext.install(converter)

    def test_real_star_is_not_empty_math(self):
        text,_=converter.preserve_environments(r'Let \(*\) denote Dirichlet convolution.')
        raw=converter.run(['pandoc','-f','latex','-t','json'],data=text)[0]
        nodes=list(converter.nodes(json.loads(raw),'Math'))
        self.assertEqual([n['c'][1] for n in nodes],['{*}'])

    def test_unexplained_empty_math_is_rejected(self):
        with self.assertRaises(ValueError):
            converter.separate_math_from_digits([{'t':'Math','c':[{'t':'InlineMath'},'']}])

    def test_inline_literal_star_is_refused_not_modified(self):
        for text in [r'\verb|\(*\)|',r'\verb*|\(*\)|']:
            with self.assertRaises(ValueError):converter.preserve_environments(text)

    def test_cache_integrity_covers_status_and_report(self):
        from prepare_sources import cache_integrity,require_cache_payload
        original={'conversion_status':'CONVERSION_BLOCKED','markdown':'','record':'','report':{}}
        changed=dict(original,conversion_status='FULL_TEX_TO_MARKDOWN_MECHANICAL')
        self.assertNotEqual(cache_integrity(original),cache_integrity(changed))
        self.assertNotEqual(cache_integrity(original),cache_integrity(dict(original,report={'changed':True})))
        with self.assertRaises(ValueError):require_cache_payload(changed)

    def test_literal_environment_is_preserved(self):
        code='\\begin{verbatim}\n\\begin{proof}not a proof\\end{proof}\n\\end{verbatim}\n'
        out,catalog=converter.preserve_environments(code)
        self.assertEqual(out,code); self.assertEqual(catalog,[])

    def test_commented_verbatim_does_not_hide_live_conditional(self):
        code='% \\begin{verbatim}\n\\iffalse\n% \\end{verbatim}\n\\input{fake}\n\\fi\n'
        with self.assertRaises(ValueError):includes.require_static_input_context(code)

    def test_external_command_in_literal_block_is_rejected(self):
        with self.assertRaises(ValueError):
            includes.require_static_input_context('\\begin{verbatim}\n\\input{fake}\n\\end{verbatim}\n')

    def test_unclosed_literal_block_is_rejected(self):
        with self.assertRaises(ValueError):ext.verbatim_spans('\\begin{verbatim}\nhello')

    def test_display_math_keeps_comment_newline(self):
        text='a% note\n+b'
        self.assertEqual(ext.normalize_math_newlines(text,display=True),text)

    def test_inline_comment_newline_is_rejected(self):
        with self.assertRaises(ValueError):ext.normalize_math_newlines('a% note\n+b')

    def test_comment_free_inline_whitespace(self):
        self.assertEqual(ext.normalize_math_newlines('a\n+b'),'a +b')

    def reference(self, ref, text=None, extra=False):
        attrs=[['reference-type','ref'],['reference',ref]]
        if extra:attrs.append(['unexpected','keep-me'])
        return {'t':'Link','c':[['',[],attrs],[{'t':'Str','c':text or '['+ref+']'}],['#'+ref,'']]}

    def test_reference_custom_text_is_not_discarded(self):
        node=self.reference('a,%\nb',text='custom text')
        with self.assertRaises(ValueError):
            converter.remap_links([node],Path('/tmp/nonexistent'),r'\label{a}\label{b}')

    def test_reference_extra_attribute_is_rejected(self):
        node=self.reference('a,%\nb',extra=True)
        with self.assertRaises(ValueError):
            converter.remap_links([node],Path('/tmp/nonexistent'),r'\label{a}\label{b}')

    def test_reference_does_not_join_internal_label_space(self):
        node=self.reference('a b,%\nc')
        with self.assertRaises(ValueError):
            converter.remap_links([node],Path('/tmp/nonexistent'),r'\label{ab}\label{c}')

    def test_output_citation_brackets_are_prose_not_display_math(self):
        from markdown_adapter import adapt
        output,report,formulas=adapt(r'Text $a+b$ and `\cite{KnownKey}`.',
            origin=Path('/tmp/example.md'), destination='example.md',owner='test',
            mapper=lambda target,*args:target,
            citation=lambda *args:'references.md#known')
        self.assertEqual(report['math_nodes'],1)
        self.assertTrue(report['math_roundtrip'])
        self.assertIn('KnownKey',output)
        self.assertEqual(formulas,[{'kind':'InlineMath','tex':'a+b'}])

    def test_pandoc_reading_layer_label_is_not_math(self):
        from markdown_adapter import adapt,OUTPUT_READER
        output,report,formulas=adapt(r'**Definition**<span id="def:test">\[def:test\]</span> $x$',
            origin=Path('/tmp/main.md'),destination='example.md',owner='test',
            mapper=lambda target,*args:target,citation=lambda *args:'references.md',
            source_reader=OUTPUT_READER)
        self.assertEqual(report['math_nodes'],1)
        self.assertEqual(formulas,[{'kind':'InlineMath','tex':'x'}])
        self.assertIn('def:test',output)

    def test_citation_qualifiers_remain_visible(self):
        from markdown_adapter import adapt,OUTPUT_READER
        raw=r'Use `\citet[Theorem~3.1]{KnownKey}` here.'
        output,report,_=adapt(raw,origin=Path('/tmp/main.md'),destination='example.md',owner='test',
            mapper=lambda target,*args:target,citation=lambda *args:'references.md',source_reader=OUTPUT_READER)
        self.assertIn(r'\citet[Theorem~3.1]{KnownKey}',output)
        self.assertTrue(report['literal_code_roundtrip'])

    def test_code_block_leading_blank_line_is_preserved(self):
        from markdown_adapter import adapt,OUTPUT_READER
        raw='`````\n\n## Historical example\n\n```text\nsome content\n`````\n'
        _,report,_=adapt(raw,origin=Path('/tmp/note.md'),destination='example.md',owner='test',
            mapper=lambda target,*args:target,citation=lambda *args:'references.md',source_reader=OUTPUT_READER)
        self.assertTrue(report['literal_code_roundtrip'])

if __name__=='__main__':unittest.main()
