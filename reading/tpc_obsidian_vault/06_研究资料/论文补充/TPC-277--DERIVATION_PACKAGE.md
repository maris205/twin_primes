---
type: "source-reading"
source_path: "papers/tpc-277-four-packet-gain-floor/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-277"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-277-four-packet-gain-floor/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-277|TPC-277]] · [[00_开始阅读|首页]]

# TPC-277 derivation package

## 1. Four-packet geometry

Let `V_0,...,V_3` be vectors in a real or complex Hilbert space. Put

```text
D = sum_j ||V_j||^2,
S = V_0+V_1+V_2+V_3,
G = ||S||^2,
E = sum_{j<k} Re <V_j,V_k>.
```

Then `G=D+2E`. Cauchy–Schwarz gives

```text
G <= (sum_j ||V_j||)^2 <= 4D.
```

When `E<=0`, `G<=D`. For `G>0`, define

```text
r=D/G,  kappa=(D-G)/D=-2E/D.
```

The exact coordinate change is `r=(1-kappa)^(-1)`.

## 2. Sharpness and the missing asymptotic input

Four equal aligned packets attain `r=1/4`; four nonzero orthogonal packets attain `r=1`. Thus geometry alone cannot produce a positive exponent in a bound `r>=b x^gamma`: an orthogonal family has `r=1` for every `x`. Large gain requires `kappa` to approach one, equivalently `G/D` to approach zero. Merely proving `E<=0` supplies only the constant floor `r>=1`.

## 3. Exact source replay

For each declared row, the certificate constructs the actual beta source and prime shell from TPC-268, accumulates the four packet outputs, applies the three declared Haar contrasts to the output vectors, and computes `D,G` with exact rational arithmetic. Outward intervals at grid `10^15` are stored; the exact pair `(D,G)` is represented by a SHA-256 replay digest. The independent checker recomputes the pair with the column-major accumulation order.

## 4. Firewall

The eight rows establish neither a uniform lower bound nor a power law. The one-percent floor fails at the smallest-gain row, but this is only a finite registered/extended obstruction. No arithmetic cancellation, `L2` estimate, full Gate-B payment, or twin-prime result is inferred.
