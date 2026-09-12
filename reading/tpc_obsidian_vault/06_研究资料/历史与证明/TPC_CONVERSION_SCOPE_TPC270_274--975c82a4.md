---
type: "source-reading"
source_path: "research/tpc-big-road/TPC_CONVERSION_SCOPE_TPC270_274.md"
snapshot_date: "2026-09-12"
owner: "DOC-975c82a45bd12508"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/research/tpc-big-road/TPC_CONVERSION_SCOPE_TPC270_274.md.txt)；可用外部编辑器核对。


[[00_开始阅读|首页]] · [[05_综合与进展/历史总结校注|历史与当前状态的区别]]

# TPC270–274 conversion and bounded prerequisite audit

Updated 2026-09-07. Source lock: `6be994e34a06fda0de2ed0bcaa42ff3db716ffef`. All five complete TeX manuscripts, README files, proof packages, and bibliography sidecars were read. Original scientific files, hand-edited materials, code, certificates, and local build products remain unchanged.

## Conversion evidence and delimiter repair

All five mechanical reading layers pass abstract/body formula-sequence and normalized-text roundtrip checks: 321 math nodes and 52 raw-source display blocks across 19 extracted PDF pages. Every source section has a unique heading-text page match. All manuscripts use inline bibliography items, retained in the reading layers; unused external BibTeX sidecars are unchanged. No bibliographic verification, visual PDF certification, or proof of PDF/TeX synchronization is claimed.

The initial conversion correctly failed closed for TPC270 and TPC271. Pandoc wrote adjacent numeric text and inline math as `64$\to$128`, but its Markdown reader does not accept that closing dollar before a digit. This misparsed subsequent delimiters and changed the formula sequences from 67 to 65 and from 54 to 53 nodes, respectively. The [converter](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/research/tpc-big-road/maintain_source_markdown.py.txt) now inserts a whitespace AST node between inline math and immediately following digit-led text. Each of these two manuscripts needs four such separators; all mathematical expressions, numbers, table cells, and original TeX remain unchanged. This handling is explicit in their conversion limitations.

The focused [regression suite](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/research/tpc-big-road/test_source_markdown_maintenance.py.txt) passes 24 tests, including whitespace-only/idempotent repair, unchanged safe boundaries, a quoted table roundtrip, and the complete TPC270 conversion. Read-only regeneration of all 144 earlier TPC275–418 conversion pairs remains byte-identical, covering their 7,659 math nodes. No previous reading layer or provenance record needed rewriting.

No original scientific producer, stress suite, physical/interval replay, or publication cascade was run. The bounded checks below use small standalone examples, saved-endpoint comparisons, and one source-code classification inspection. Saved scientific certificates are not re-proved.

## Per-paper formula and prerequisite review

| Paper  | Source location                                                                                                                                                                                                                                                                                                                                                                 | Bounded check and limit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TPC270 | [literal source](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-27bc230ef4383658); [normalization](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-f3234177780132c3); [ratio](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-7d3a2281bbf0bcc9)                    | Four equal blocks of N/2 coordinates require N divisible by eight, not only even; all listed scales satisfy this. The comparison definition includes the following prose zeroing rule, not only its displayed product. Positive N and valid radius-square enclosures justify cubing; interval division additionally requires a strictly positive denominator enclosure. The statistic is the sixth power of normalized radius, not the raw radius or radius square.                                                       |
| TPC271 | [residual coordinates](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-7844413d043efdc4); [lane identities](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-de6317e67d7534ec); [profile controls](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-0a7234d44d7340b4) | W and G are squared norms. Their product defines R squared and their cubed normalized coordinates multiply to Xi. Nonzero C is needed for inverse amplification, not for the direct lane-product identity. All vectors and the projection use the same inner product. Unchanged w and P3 give unchanged source lane under profile changes; separately evaluated interval quotients need not be exactly the singleton one. Negative scalar argument and the magnitude of normalized correlation are different information. |
| TPC272 | [margin identity](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-08c7b85d96350cfa); [compiler](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-8e9af3c0ba808ebe); [sign-only construction](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-22ab6b2f52551a2c)       | R\>0 defines m; m\>0 excludes C=0 when using R=abs(C)/m or the inverse sixth power. Cauchy–Schwarz gives m≤1 only for the same Hilbert-space scalar and norm lanes. The compiler assumes common-source estimates valid for all sufficiently large x and sufficiently small epsilon; finite data do not supply either hypothesis. The two-dimensional construction keeps W,G fixed and realizes every 0\<m≤1, but does not realize the constrained literal arithmetic family.                                              |
| TPC273 | [margin transfer](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-c680d17d18cd4c92); [band definitions](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-635eef8e3a348d48); [finite transitions](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-d19c895af77d5b72)   | The pointwise relation m squared=rho squared requires positive residual denominators and the nonnegative margin definition. Valid nonnegative enclosures transfer monotonically by cubing. Certifying neither low nor high does not itself certify the middle band: a straddling interval needs an unresolved category or an additional containment check. Cutoff-only comparisons fix the matrix and beta at fixed N,s; changing kernel exponent changes matrix entries.                                                 |
| TPC274 | [projection](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-0e9e2988883c0ae1); [Frobenius theorem](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-2c5b7c7e0032b958); [margin ordering](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-894f56f9a62c2125)          | Matrix/vector dimensions and Euclidean norms must match. Rowwise Cauchy–Schwarz works over reals or complexes and needs no randomness. The raw inequality also holds at zero, but positive W,G are needed for gain and margin quotients; then the envelope is positive. A small lower proxy cannot upper-bound the actual margin. The exact Frobenius numerator and transferred interval denominator remain different evidence types.                                                                                     |

## TPC270–271: normalization and displayed intervals

For an elementary normalization example, take N=8,R=32 and N=64,R=512. The raw radius grows by 16, yet Xi falls from 1 to 1/64 because the normalized radius halves. Thus a displayed normalized-sixth-power drop cannot be read as the same-factor raw-radius drop. A same-scale profile ratio of Xi is likewise the sixth power of the radius ratio. The separate floating implementation described in the [TPC270 proof](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-013dfe6133d781da) is an audit of numerical agreement, not a replacement for rigorous outward enclosures. Its distinction is correctly explicit in the proof package.

A read-only exact-fraction comparison confirms that all six TPC270 printed base intervals agree with their saved counterparts, including scientific-notation versus ordinary-decimal spellings. This is a display comparison only; source weights and interval arithmetic were not replayed.

TPC271 [says](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-927ee23a791054c5) that all table endpoints are outward enclosures. Of its twelve displayed lane-ratio intervals, two fail to contain the saved TPC271 intervals:

| Pair and field            | Printed interval      | Saved interval                    |
|---------------------------|-----------------------|-----------------------------------|
| 64→128, output lane       | \[0.633926,0.633926\] | \[0.633925939307,0.633925939307\] |
| 64→128, radius coordinate | \[0.231754,0.231847\] | \[0.231753859227,0.231847466257\] |

The first displayed singleton is displaced; the second interval is narrower at both ends. Neither is an outward rounding of the saved interval. This does not prove the exact physical value lies outside the display, or that the saved singleton is itself a valid exact enclosure. All original endpoints are preserved, with their comparison scope stated here.

The amplification Xi/Xi\_C measures inverse absolute normalized correlation, not the scalar’s complex argument alone. For w=(1,0), g=(−3/5,4/5), the squared norms are both one, C=−3/5 has negative-real phase, m=3/5, and amplification is `15625/729=(5/3)^6`. Arbitrarily small negative correlations have the same phase label but different amplification. No statistical independence is implied; the manuscript explicitly declines it.

## TPC272: epsilon payment and powered thresholds

The compiler carries two epsilon losses. Put `gap=sigma−eta−1/400>0`; the necessary choice in its upper-bound argument is `0<epsilon<gap/2`. The [proof wording](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-fbdf49586a19e527) and [proof package](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-69e0a1149fd66103) say epsilon is below the strict gap. This can be satisfied by choosing below half the gap, but mere `epsilon<gap` is not enough for the stated exponent: gap=1/400 and epsilon=3/1600 satisfy that weaker inequality while 2epsilon exceeds the gap. The endpoint implication also requires the hypotheses to remain available for the sufficiently small epsilon chosen, not just one previously fixed large epsilon.

Direct checks give `(1/8)^6=1/262144` and `(1/32)^6=1/1073741824`. The finite dyadic statistic is a ratio of sixth powers; a ratio below `(1/32)^6` corresponds to a margin ratio below 1/32 when both margins are positive. It is not itself the unsquared margin ratio. No nine-row transfer was recomputed.

## TPC273: classification gap versus the actual saved middle rows

The inspected [classification function](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-0ff4e03b3bcc235c) returns low if the upper squared-margin endpoint is below 1/64, high if the lower endpoint exceeds 1/16, and middle otherwise. As a general interval classifier, that last branch does not prove `1/64≤m^2≤1/16`. For example `[1/128,1/32]` enters the middle branch but contains the value 1/100, which lies in the low band. The exact-value trichotomy and an interval certification are different.

The actual [saved certificate](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-273-margin-stability-matrix/results/tpc273_certificate.json.txt) contains eleven middle-labeled rows. A read-only fraction check shows all eleven of their stored squared-margin intervals are contained in `[1/64,1/16]`. Thus the classifier’s general insufficiency does not refute the saved eleven-row middle census. This endpoint check assumes the saved enclosures; it does not revalidate their physical construction, the remaining phase census, or the 32-row producer.

The [abstract’s clock language](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-abfcdf64db031016) does not mean there is an independent H perturbation at each N: the grid has four fixed `(N,H,Q)` triples times four z values times two s values. H changes with scale, not as a third within-scale control axis. The matrix is fixed across cutoff-only comparisons, but not across changes in s. These distinctions preserve the main two fixed-N,s cutoff transitions without broadening their scope. The literal `qquad` at [TeX line 100](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-052cb97b08024054) is unchanged. The inline bibliography key `TPC273` labels a TPC272 entry; the printed reference text remains authoritative, not the key name.

## TPC274: the lower proxy does not upper-bound the margin

Take B=diag(1,100), beta=(1,0), and w=(1,0), with no projection in this generic example. Then G=1,C=1,W=1, while the Frobenius envelope is G\_F=10001. The actual squared margin is one, whereas the proxy is `1/10001<1/64`. This verifies why a loose upper output envelope can produce a small conservative margin proxy without ruling out large actual correlation. It is not an actual V59 row or evidence about its twelve numerical gaps.

The [abstract](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-0f64b9e0c9ca44d6) says “three-block Haar projection”; the main definition correctly uses three contrasts across four blocks. The main definition must not be replaced by a three-source-block interpretation. The literal `qquad` at [TeX line 86](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-975c82a45bd12508.md#src-247ebfdeb98440f2) remains unchanged. The margin-ordering statement in the proof package correctly includes positive W and G.

## Supplemental source locks and continuation

All inspected supplemental artifacts equal the source-commit bytes:

| Artifact                  | SHA-256                                                            |
|---------------------------|--------------------------------------------------------------------|
| TPC270 saved result       | `3cdb6ca037c0a93c85ad2de225483e486db8da33893ec54ba9e274b0a5443e55` |
| TPC271 saved result       | `fa981eeec9f0f618081af0fdc86fd3a1f29cf3d221916b3e3036a659ef676100` |
| TPC273 saved result       | `e44287f82692d4be536665cb87a4092d45fa48381a809a7efbdf66d67c962d13` |
| TPC273 inspected producer | `9898d54a8c36c1c9576961a0f246ab6201c1a88997e9537a667e0537c27ff7a9` |

This batch raises mechanical full-source coverage from 144 to 149 and reduces partial/notes entries from 678 to 673. The converted contiguous range is TPC270–418, with 7,980 mechanically preserved math nodes. Across all 823 entries, `reliable-full-md=0` and `source-inaccessible=1` remain unchanged.

Bounded prerequisite checks and conversion regression tests are not independent full-content mathematical verification. No source theorem, certificate, claim grade, or TPC418 STOP condition is changed, and no new paper number is created.
