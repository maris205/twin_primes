---
type: "source-reading"
source_path: "papers/tpc-280-leakage-aware-endpoint-compiler/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-280"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-280-leakage-aware-endpoint-compiler/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-280|TPC-280]] · [[00_开始阅读|首页]]

# TPC-280 proof package

## Conditional two-term compiler

Assume `D >= dX^a` and `G <= BX^(-gamma)D+ell X^(a-delta)`. Since `D>0`, division and the source floor imply

`G/D <= BX^(-gamma)+(ell/d)X^(-delta)`.

For `G>0`, taking positive reciprocals gives

`D/G >= [BX^(-gamma)+(ell/d)X^(-delta)]^(-1)`.

Set `kappa=min(gamma,delta)`. Since `X>=1`, both powers are at most `X^(-kappa)`, hence the denominator is at most `(B+ell/d)X^(-kappa)`, proving the collapsed compiler. The zero-coefficient case is interpreted separately as `G=0`.

## Margin transfer

The exact four-packet identity from the parent interface is `m^2=(D/G)m_D^2`. Substitution of the two-term reciprocal bound proves the two-term margin inequality. Substitution of `m_D>=cX^(-eta_D-epsilon)` and the collapsed gain bound proves the exponent `-eta_D+kappa/2-epsilon`; replacing a negative effective loss by zero gives `eta_eff=max(0,eta_D-kappa/2)`.

## Sharpness and obstruction

The equality family in `DERIVATION_PACKAGE.md` saturates the source floor and the raw output bound, so no uniformly smaller two-term denominator follows from these hypotheses. With `delta<gamma` and positive leakage, the second term has the slower decay and prevents promotion to exponent `gamma`. The certificate also tests the borderline endpoint equality: `sigma-eta_eff=1/400` is not a strict payment.
