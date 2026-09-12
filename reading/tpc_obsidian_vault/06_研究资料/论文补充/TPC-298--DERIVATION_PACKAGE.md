---
type: "source-reading"
source_path: "papers/tpc-298-profile-angle-dimension-ladder/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-298"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-298-profile-angle-dimension-ladder/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-298|TPC-298]] · [[00_开始阅读|首页]]

# TPC-298 derivation package

Let `I` be the frozen finite source interval, `S` the prime shell, and let `A` be the rational matrix whose column `q` is the physical vector `g_q`. For the ordered cutoff list `Z=(z_1,...,z_K)`, define

```text
u_j(t) = lambda(t) - sum_{d<=z_j, d|t} mu(d),
U_k = [u_1 ... u_k],
V_k = A^T U_k.
```

For a target `b` and a full-column-rank `V_k`, put

```text
c_k = (V_k^T V_k)^(-1) V_k^T b,
P_k = V_k (V_k^T V_k)^(-1) V_k^T.
```

Then

```text
||b-V_k c_k||^2 = b^T(I-P_k)b,
cos^2(theta_k) = b^T P_k b / ||b||^2,
r_k = ||b-V_k c_k||/||b|| = sin(theta_k).
```

Because `range(V_k) subset range(V_{k+1})`, orthogonal projection gives `r_{k+1} <= r_k` and `theta_{k+1} <= theta_k`. If `k=|S|` and the row has full row rank, `P_k=I` on the target space and the finite residual is zero.

For a threshold `tau`, define

```text
k_tau(b) = min { k : r_k <= tau }.
```

This is a finite definition. It becomes an asymptotic theorem only after uniform rank, conditioning, target identification, and source-budget bounds are proved; none of those upgrades is taken here.
