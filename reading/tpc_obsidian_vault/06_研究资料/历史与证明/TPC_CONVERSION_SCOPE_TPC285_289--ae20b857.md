---
type: "source-reading"
source_path: "research/tpc-big-road/TPC_CONVERSION_SCOPE_TPC285_289.md"
snapshot_date: "2026-09-12"
owner: "DOC-ae20b8572e7f8aac"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/research/tpc-big-road/TPC_CONVERSION_SCOPE_TPC285_289.md.txt)；可用外部编辑器核对。


[[00_开始阅读|首页]] · [[05_综合与进展/历史总结校注|历史与当前状态的区别]]

# TPC285–289 conversion and bounded prerequisite audit

Updated 2026-09-07. Source lock: `c9f2a3559e421cb10eaf51c1268a03b838c5ed68`. All five complete TeX manuscripts, README files, proof packages, and external bibliographies were read. Original scientific files, hand-edited materials, code, certificates, and local build products remain unchanged.

## Conversion evidence

The five mechanical reading layers pass abstract/body formula-sequence and normalized-text roundtrip checks: 454 math nodes and 77 raw-source display blocks across 27 extracted PDF pages. Per-paper records lock source/PDF/ BibTeX hashes, give source-line maps and formula catalogues, and link this scope note. Full external bibliographies are retained as BibTeX; their claims and citation keys are not independently verified or resolved.

Four automatic heading maps remain explicitly uncertain. Direct extracted- line inspection supplies the following bounded manual supplements:

| Paper / original source section                 | Automatic state         | Manual extracted heading                |
|-------------------------------------------------|-------------------------|-----------------------------------------|
| TPC286, `Reproducibility details`, TeX line 322 | Unmapped                | `A Reproducibility details`, PDF page 5 |
| TPC287, `Reproduction record`, TeX line 420     | Unmapped                | `A Reproduction record`, PDF page 6     |
| TPC288, `Conclusion`, TeX line 448              | Ambiguous pages 1 and 6 | `9 Conclusion`, PDF page 6              |
| TPC288, `Reproduction record`, TeX line 464     | Unmapped                | `A Reproduction record`, PDF page 7     |

The appendix letters are not stripped by the current automatic matcher. These manual observations do not silently change that matcher or certify PDF/TeX synchronization. All other section maps in this batch have unique heading-text matches. No PDF rebuild or visual publication QA is claimed.

No source producer, full scientific checker, full modular rank computation, physical Gram reconstruction, or publication cascade was run. Read-only code inspection, one literal operator entry, and standalone small algebraic examples below are the whole additional check scope; they do not revalidate published rank, interval, spectrum, or census certificates.

## Per-paper formula and prerequisite review

| Paper  | Source location                                                                                                                                                                                                                                                                                                                                                                          | Bounded check and limit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TPC285 | [residue factorization](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-95fd3fb08d184b84); [deletion theorem](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-7301d5cca803f8fe); [modular scope](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-fea9c5a4bbbd936e)           | Odd q gives m=q−1\>1. Nonempty disjoint residue columns give full column rank when every class occurs; the centered projection has rank q−2. Class counts are positive integers, so `mn_a-(m-1)>=1`; the determinant factor is strictly negative. Restrict to active coordinates, not the identically zero multiples of q. Valid modular reduction needs every denominator invertible at a prime; full modular rank proves rational nonsingularity, not a quantitative norm estimate. Kernel-Schur full rank is separately a finite source claim.                    |
| TPC286 | [diagonal split](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-a18e3e0636d090d3); [linear attachment](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-29af73d9e960a2c6); [interval reconstruction](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-73bdc3ed86bfff28)       | The same finite shell, masks, source, and kernel give the output split; H\>0 makes K(0)=1. A fixed real weight realization gives exact scalar linearity. Ordinary interval evaluation is an enclosure procedure and is not itself linear; independently subtracted component intervals need only contain the directly computed interval. The four-block implementation separately requires positive equal block sizes and nonzero normalizers. An output correction vector is not a diagonal operator matrix.                                                        |
| TPC287 | [finite additivity](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-a390acdf9c462b74); [retention envelope](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-26d2d87fc786ec75); [uncertainty qualification](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-a8e7c6f72eb2c3d6) | Additivity holds for finite sums and a fixed linear scalar functional. For retention, require a nonempty shell as well as valid sign-separated component enclosures, so lower unsigned mass is positive. Zero separation of every component is sufficient but not necessary if an independently positive lower total is known. No probabilistic independence is required. The exact retention is at most one by the triangle inequality, whereas its conservative upper enclosure can exceed one. One-prime omission leaves zero and is not a nonzero sign reversal. |
| TPC288 | [Gram energy](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-f1b58736ac9ecc21); [modular witness](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-1b1ea61a3225af1c); [claimed active set](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-a757ab5aa420ad8b)                 | Gram symmetry/PSD and finite energy identities apply before normalization. Energy ratio needs positive Gram trace; scalar retention needs a positive unsigned scalar denominator. Modular full rank plus Gram PSD gives positive finite Gram eigenvalues, not a uniform lower bound or positivity of the deleted-diagonal physical operator. The printed intersection of masks is only a common-active restriction, not all nonzero coordinates of the aggregate; its code checks that restricted principal submatrix.                                               |
| TPC289 | [coherence](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-93e4db7fa469cf04); [ordered cross terms](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-04eb666506ed9ed5); [accumulation](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-9e1a90d99ce522bb)                     | Squared coherence requires both component energies positive and discards cross-term sign. The accumulation proof separately uses positive cross terms, nonnegative eta/delta, a nonempty shell, and defined positive diagonal normalization. The main statement supplies eta/delta in \[0,1\]; the proof-package shorthand must inherit that range. Ordered pairs contribute k(k−1) terms, not half that count. A negative cross term invalidates pairwise positivity but does not force total energy below one.                                                     |

## TPC285: rank scope and the full-class condition

For q=3 with one active coordinate in each nonzero residue class, the centered matrix is `[[1/2,-1/2],[-1/2,1/2]]`, of rank one. Deleting its diagonal gives determinant `-1/4` and rank two. If only one active coordinate is present, deletion instead gives the zero matrix: the full-class premise cannot be dropped. These are small exact illustrations of the proof, not the registered 20-row kernel-Schur rank replay.

The within-class and block-constant summands are invariant, and the latter class-value matrix need not be symmetric in that unnormalized basis. Invertibility of both summands suffices; no positive-definiteness conclusion for the deleted matrix is used. Full rank itself does not control how small singular values become or how cross-prime summands interact.

## TPC286–287: exact weight realizations versus interval arithmetic

TPC286’s [proof package](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-f8e962f7128fa9ba) calls the attachment linear because interval-valued weights are held fixed. That statement is valid pointwise for each fixed real realization of the uncertain weights, not as equality of independently evaluated intervals. For the one-coordinate linear functional `C(w,g)=wg`, take `w in [1,2]` and `g_full=g_diag=1`. The physical output is zero, so its interval is `[0,0]`, while independent subtraction gives `[1,2]-[1,2]=[-1,1]`. Shared uncertainty is duplicated by interval subtraction. This does not invalidate the exact split; it explains why the source’s [implemented comparison](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-e780b19c0bec9033) correctly tests containment rather than endpoint equality.

TPC287 explicitly preserves this distinction in its [TeX discussion](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-a8e7c6f72eb2c3d6) and [proof’s realization step](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-2b6bccbc0f810cd5). Its statement that every sign-separated component makes the lower sum positive also needs a nonempty shell; for an empty shell that condition is vacuous and both masses are zero. The exact additivity theorem still includes the empty shell, but its normalized retention theorem does not.

A small enclosure example uses components `5/2` and `-3/2`, component intervals `[2,3]` and `[-2,-1]`, and shell interval `[1,2]`. It gives `1/5 <= 1/4 <= 2/3` for lower bound, exact retention, and upper bound. Trial division through the square root also confirms the seven printed shell contents for Q=`3,4,9,10,16,22,27`, with cardinalities 1–7. Consequently the protocol sizes are `7*6*2=84` and `12*(1+2+3+4+5+6+7)=336`. No attachment or leave-one-out census is replayed.

TPC286’s [README claim line](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-6f99a0b85027935f) uses `A_phys=A_full-Delta_diag`, while its [earlier definition](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-85c901467f75d20f) makes `Delta_diag(u)` an output vector already multiplied by beta. If A denotes an operator matrix, subtract instead the diagonal matrix of the multipliers, or state the vector identity for g as the main TeX does. The notation remains unchanged and is not silently type-corrected.

## TPC288: common-active intersection is not aggregate support

The [TeX](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-1e1f57a12cf3d49c) defines the active set by `for every q in S, q does not divide u`, meaning the intersection of the individual nondivisibility masks. Its following sentence says rows and columns outside that intersection vanish for every component. That implication reverses the quantifiers: failing one component’s mask does not fail every component’s mask. The union of component masks, rather than their intersection, is the candidate support; even that candidate set does not by itself rule out aggregate cancellations or isolated zero rows.

There is a literal single-entry witness inside the first printed growth interval `I={65,...,128}`, shell `(11,13,17)`, H=24 and s=2. Coordinate u=66 is excluded by the intersection because 11 divides it, but neither 13 nor 17 does. For t=67, the 11-component entry is zero, while the 13- and 17-components are respectively `-359424/332929` and `-352512/332929`. Their aggregate is `A_shell(66,67)=-711936/332929`, which is nonzero. This entry uses only the printed operator and no source beta, output construction, or large matrix computation.

The inspected [rank routine](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-7e510fee042a4301) uses exactly `all(u % prime for prime in shell)` to select both indices. The [recorded count](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-df2f709579fb558f) uses the same intersection. Its six source-reported full-rank witnesses are therefore for these common-active principal submatrices, not a proof that the aggregate is full rank on all actual nonzero coordinates. If the restricted certificates are valid, they give rank lower bounds for the larger operator; extension to full rank needs additional evidence. The separate full-output Gram certificates are different objects and are not refuted or revalidated by this support correction.

A standalone scalar/energy illustration takes `g_1=(1,2)`, `g_2=(-1,2)` and the first-coordinate scalar functional. Scalar retention is zero, but the energy ratio is `16/10=8/5`. This checks the conceptual distinction without verifying the paper’s 13 physical rows. Literal source tokens `quad` and `qquad` without backslashes at [line 273](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-8aa0da628f7b1541) and [line 287](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-ae20b8572e7f8aac.md#src-9733a5f2614490bc) remain preserved. Four equal positive blocks additionally require interval length divisible by four; for this paper’s half interval that means N divisible by eight, stronger than the opening even-N condition. Its declared grid meets that divisibility condition.

Inspected source code matches the locked commit:

-   TPC286: SHA-256 `7e0bfead06d37941ee972e42782e5917237aa7083eae37ed891bd775cc240022`.
-   TPC288: SHA-256 `ee88cef250dc37d14b5fa5bbc22cc9cd5d0a44da6a4e4412118895b27e214987`.

## TPC289: signed rather than squared coherence drives accumulation

For two nonzero opposite vectors, squared coherence is one and diagonal balance is one, yet the aggregate energy is zero. Thus the separate positive-cross-term condition is indispensable for taking the positive square-root branch. The source’s conditional proof retains it correctly. Exact arithmetic confirms its example lower bounds `193/25` and `217/25` for 15 and 17 primes at eta=`3/5`, delta=`4/5`.

The source already warns that cutoff controls with identical signatures are not independent new asymptotic samples. Neither the eight-row positive block nor one finite sign-flip row settles an eventual growing-shell statement. Published signs, coherence values, 1,380-pair counts, and threshold certificates remain source-reported rather than re-proved here.

## Coverage and continuation

```bash
python -B research/tpc-big-road/check_source_markdown_batch.py --first 285 --last 289
```

The new total is 134 `full-source-md`, 0 `reliable-full-md`, 688 `partial-or-notes`, and 1 `source-inaccessible`, across 823 entries. TPC285–418 now have mechanical reading layers with 6,952 math nodes. Earlier scope notes remain historical batch snapshots.

Next existing-source batch: TPC280–284. TPC418’s scientific stop remains `NONE_UNTIL_GROWING_OR_PHYSICAL_GATE_CHANGES`, with arithmetic advance `NO`, fixed-power credit `0`, and full Gate B `OPEN`. Conversion creates no new number, original-source correction, theorem, or route reopening.
