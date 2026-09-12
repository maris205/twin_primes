---
type: "source-reading"
source_path: "papers/tpc-402-c1-signed-diagonal-term-audit/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-402"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-402-c1-signed-diagonal-term-audit/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-402|TPC-402]] · [[00_开始阅读|首页]]

# Derivation package

Write `D_p(u)=1_{p not divide u}` and `b_sigma(u)=sum_{p|u}sigma_p a_p`. For distinct points in a production window, `p>N` prevents a prime from dividing both points. Expanding the endpoint terms gives `sum sigma_p a_p D_p(u)D_p(v)=A_sigma-b_sigma(u)-b_sigma(v)`, hence `M_sigma(u,v)=T_uv[-A_sigma+b_sigma(u)+b_sigma(v)]`. This is exact for the finite production domain and gives no arithmetic meaning to `sigma`.
