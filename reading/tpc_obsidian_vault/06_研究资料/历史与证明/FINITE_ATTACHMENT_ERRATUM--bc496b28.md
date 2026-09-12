---
type: "source-reading"
source_path: "research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/FINITE_ATTACHMENT_ERRATUM.md"
snapshot_date: "2026-09-12"
owner: "DOC-bc496b28e3a3bee6"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/FINITE_ATTACHMENT_ERRATUM.md.txt)；可用外部编辑器核对。


[[00_开始阅读|首页]] · [[05_综合与进展/历史总结校注|历史与当前状态的区别]]

# Finite attachment erratum and scope clarification

Date: 2026-09-09. Parent integration of the independent Maxwell audit. The original reconnaissance report is preserved verbatim, not silently corrected.

Affected source: research/tpc-big-road/research-rounds/2026-09-09-multi-agent-recon/agent-reports/recon-physical-attachment.md.

With row $u$, column $t$, the physical kernel is $K_{H_x}(u-t)$. The correct star entries are $$  (A_J)_{0r}=-C_-K_{H_x}(-r),\qquad  (A_J)_{r0}=-C_-K_{H_x}(r)\quad(r\ge1). $$ The upper entry in the original report omitted the minus in the kernel argument. Realness of the profile gives conjugate symmetry, not evenness. The later definition $F_{rs}=K_{H_x}(r-s)/T_{r-s}$ in that report was already correctly oriented. Therefore its finite factorization $A_J=\lambda R(F\circ M)R$ and the resulting real-lane pairing survive with the displayed star corrected.

The $A=0$ caveat requires a nonzero corresponding physical interior entry: entrywise multiplication and diagonal congruence cannot create one from a zero model interior. It is not a universal impossibility statement. Moreover a single complete ordered shell with strictly increasing amplitudes has nonzero alternating sum, negative for even cardinality and positive for odd cardinality. The $A=0$ caveat is inapplicable within that single-shell domain.

The audit also verifies: $$  \|F\circ Z_{\mathrm{model}}\|<17\|\psi_+\|_1\|Z_{\mathrm{model}}\|,  \qquad  \|R\|^2=  \max\{C/|A|,\ C_-^2|A|/(P_-^2C)\}. $$ The factor $C/|A|$ cancels the model alternating-bulk gain in this norm transfer. It does not rule out a different coefficient-sensitive argument.

The exact full-shell endpoint-CRT no-cover obstruction remains valid. If $J\subset I_x$ and all selected shell primes divide the two external endpoints $o(o+n)$, their product is at most $x(x+1)$. Seven distinct primes greater than $x^{1/3}$ already have product greater than $x^{7/3}>x(x+1)$ for $x\ge8$. Thus the construction cannot supply such physical windows when the physical shell has at least seven primes. Arbitrarily large CRT origins do not repair an origin restriction.

The old audit’s statement that the hybrid and profile were not yet fully recovered is historical task-time scope, not the final state of this round. The recovered source definitions are in DERIVATION\_PACKAGE.md. None of these corrections changes the no-GO boundary or proves a physical cover, a physical model-height identification, or fixed-power cancellation.

Full independent proof and finite exact checks: agent-reports/physical-loop-finite-attachment-audit.md.
