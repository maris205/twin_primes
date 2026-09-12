---
type: "source-locator"
generated: true
---


# DOC-ae20b8572e7f8aac 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-04eb666506ed9ed5

`papers/tpc-289-cross-prime-gram-coherence/paper/main.tex`，原始第 103 行。

````text
101: The square records the size of a cross term independently of its sign; the
102: sign of $G_{q,r}$ is retained as a separate datum.  Expanding the aggregate
103: square gives the exact energy decomposition
104: \begin{equation}
105:  \frac{\norm{g_S}_2^2}{\sum_{q\in S}d_q}
106:  =1+\frac{\sum_{q\ne r}G_{q,r}}{\sum_{q\in S}d_q},
107:  \label{eq:energy}
108: \end{equation}
````

## src-1b1ea61a3225af1c

`papers/tpc-288-growing-shell-gram-obstruction/paper/main.tex`，原始第 199 行。

````text
197: $R_E$ contains all cross terms of the output Gram matrix.
198: 
199: \begin{proposition}[finite modular spectral witness]
200: Let $M$ be a rational square matrix whose entry denominators are units modulo
201: a prime $p$.  If its reduction has full rank over $\Fp$, then $M$ is
202: nonsingular over $\mathbb Q$.  Consequently, if a rational Gram matrix is
203: positive semidefinite and has full modular rank, all of its real eigenvalues
204: are strictly positive.
````

## src-1e1f57a12cf3d49c

`papers/tpc-288-growing-shell-gram-obstruction/paper/main.tex`，原始第 216 行。

````text
214: For the aggregate physical matrix, define the active set
215: \begin{equation}
216:  \activeset=\{u\in I:q\nmid u\text{ for every }q\in\shell\}.
217:  \label{eq:active}
218: \end{equation}
219: Rows and columns outside this set vanish for every component.  A full-rank
220: modular witness for $A_{\shell}|_{\activeset}$ therefore certifies a full-rank
221: physical block on its actual nonzero coordinates.
````

## src-26d2d87fc786ec75

`papers/tpc-287-prime-shell-cancellation-depth/paper/main.tex`，原始第 169 行。

````text
167: \end{remark}
168: 
169: \section{A certified retention envelope}
170: 
171: Let $c_q=C(w,g_q)$ and $c_{\shell}=C(w,g_{\shell})$.  Suppose interval
172: computations provide valid enclosures $J_q=[\ell_q,u_q]$ and
173: $J_{\shell}=[\ell_{\shell},u_{\shell}]$.  Assume each $J_q$ is separated from
174: zero.  Define
````

## src-29af73d9e960a2c6

`papers/tpc-286-diagonal-deletion-attachment-ledger/paper/main.tex`，原始第 115 行。

````text
113: The first sum includes the $t=u$ terms; the second one does not.
114: 
115: The scalar used in the finite certificates is the four-block projected
116: attachment.  If $w$ is the interval-valued source weight and $g$ is an output,
117: write
118: \begin{equation}
119:  C(w,g)=\sum_{u\in I}w(u)g(u)
120:  -\sum_{r=1}^{3}\frac{W_r(w)G_r(g)}{d_r},
````

## src-2b6bccbc0f810cd5

`papers/tpc-287-prime-shell-cancellation-depth/PROOF_PACKAGE.md`，原始第 111 行。

````text
109: ### Step 3: lower and upper unsigned masses
110: 
111: Choose any admissible realization of the interval-valued source weights.  Since
112: $c_q\in J_q$ and each $J_q$ is sign-separated,
113: 
114: $$
115: |c_q|\geq \operatorname{dist}(0,J_q),
116: \qquad
````

## src-6f99a0b85027935f

`papers/tpc-286-diagonal-deletion-attachment-ledger/README.md`，原始第 31 行。

````text
29: 
30: ```text
31: PROVED_EXACT = A_phys = A_full - Delta_diag and C_phys = C_full - C_diag
32: NUMERICALLY_CERTIFIED_FINITE = 72-row component/sign/sensitivity ledger
33: NUMERICALLY_CERTIFIED_FINITE = 15 full-versus-physical sign flips
34: NUMERICALLY_CERTIFIED_FINITE = 21 strict diagonal-dominance rows
35: OPEN = asymptotic diagonal dominance
36: OPEN = signed full-shell cancellation or literal arithmetic L2
````

## src-7301d5cca803f8fe

`papers/tpc-285-prime-shell-residue-rank-obstruction/paper/main.tex`，原始第 107 行。

````text
105: \section{Diagonal deletion restores full active rank}
106: 
107: Let $J_q=\{u\in I:q\nmid u\}$ and let $n_a$ be the number of indices in
108: $J_q$ congruent to $a$ modulo $q$.  Assume $n_a>0$ for every
109: $a=1,\ldots,m$, where $m=q-1$.  On the active coordinates, multiply $D_q$ by
110: $m$.  Since the diagonal entry of $mB_q$ is $m-1$, we obtain
111: \begin{equation}
112:  M_q:=mD_q=mR_qR_q^{\mathsf T}-u_qu_q^{\mathsf T}-(m-1)I,
````

## src-73bdc3ed86bfff28

`papers/tpc-286-diagonal-deletion-attachment-ledger/paper/main.tex`，原始第 222 行。

````text
220: \end{table}
221: 
222: The decomposition is computationally meaningful, not just notational.  The
223: full and physical signs differ in 15 rows.  In 30 rows the diagonal correction
224: has the opposite sign from the physical attachment, and in 21 rows its
225: certified absolute lower bound is strictly larger than the physical absolute
226: upper bound.  The conservative ratio lower bound exceeds $2$ in 13 rows and
227: $10$ in 4 rows.  Exact interval subtraction confirms that the reconstructed
````

## src-7e510fee042a4301

`papers/tpc-288-growing-shell-gram-obstruction/code/tpc288_growing_shell_gram_certificate.py`，原始第 275 行。

````text
273: 
274: 
275: def active_operator_rank(indices: list[int], height: int, shell: list[int],
276:                          exponent: int) -> tuple[int, int]:
277:     """Return (active dimension, modular rank) of the aggregate operator."""
278:     active = [u for u in indices if all(u % prime for prime in shell)]
279:     matrix: list[list[int]] = []
280:     h_power = pow(height, 2 * exponent, MODULUS)
````

## src-85c901467f75d20f

`papers/tpc-286-diagonal-deletion-attachment-ledger/README.md`，原始第 18 行。

````text
16: - states and proves the exact linear decomposition needed after the
17:   TPC-285 rank obstruction;
18: - gives the diagonal output in closed form,
19:   `Delta_diag(u) = sum_q q K_H(0)(q-2)/(q-1) m_q(u) beta(u)`;
20: - replays the complete six-control, six-baseline, two-exponent atlas rather
21:   than selecting only the earlier sign-flip rows;
22: - separates a structural identity from a finite sensitivity ledger, with
23:   outward interval arithmetic and an independent checker;
````

## src-8aa0da628f7b1541

`papers/tpc-288-growing-shell-gram-obstruction/paper/main.tex`，原始第 273 行。

````text
271: \begin{equation}
272:  m^- =\sum_q a_q^-,\quad
273:  m^+=\sum_q a_q^+,quad
274:  R_C^- =\frac{a_{\shell}^-}{m^+},\quad
275:  R_C^+ =\frac{a_{\shell}^+}{m^-}.
276:  \label{eq:ret}
277: \end{equation}
278: When $m^->0$, interval inclusion gives
````

## src-93e4db7fa469cf04

`papers/tpc-289-cross-prime-gram-coherence/paper/main.tex`，原始第 97 行。

````text
95: deleted diagonal, and prime shell are exactly those inherited from TPC-288.
96: 
97: For $q\ne r$ with $d_qd_r>0$, define
98: \[
99:  \Gamma_{q,r}=\frac{G_{q,r}^2}{d_qd_r}.
100: \]
101: The square records the size of a cross term independently of its sign; the
102: sign of $G_{q,r}$ is retained as a separate datum.  Expanding the aggregate
````

## src-95fd3fb08d184b84

`papers/tpc-285-prime-shell-residue-rank-obstruction/paper/main.tex`，原始第 81 行。

````text
79: \section{Exact centered factorization}
80: 
81: \begin{theorem}[residue-mode factorization]
82: For every odd prime $q$ and finite index set $I$,
83: \begin{equation}
84:  B_q=R_qP_qR_q^{\mathsf T},\qquad
85:  P_q=I_{q-1}-\frac{{\bf1}{\bf1}^{\mathsf T}}{q-1}.
86:  \label{eq:factor}
````

## src-9733a5f2614490bc

`papers/tpc-288-growing-shell-gram-obstruction/paper/main.tex`，原始第 287 行。

````text
285: The output energy is computed before decimal serialization:
286: \begin{equation}
287:  E_{\mathrm{diag}}=\sum_{q,u}g_q(u)^2,qquad
288:  E_{\mathrm{shell}}=\sum_u\left(\sum_qg_q(u)\right)^2.
289:  \label{eq:exactenergy}
290: \end{equation}
291: The ratio $R_E$ is therefore exact rational data.  The output Gram is reduced
292: modulo $p=1\,000\,000\,007$ and row-reduced.  On the finite grid all
````

## src-9e1a90d99ce522bb

`papers/tpc-289-cross-prime-gram-coherence/paper/main.tex`，原始第 131 行。

````text
129: \end{proof}
130: 
131: \begin{proposition}[Conditional coherence accumulation]
132: Let $k=|S|$, $d_- =\min_{q\in S}d_q$, and
133: $d_+=\max_{q\in S}d_q$.  Suppose that for some $0\leq\eta,\delta\leq1$,
134: \[
135:  G_{q,r}>0,\qquad \Gamma_{q,r}\geq\eta^2\quad(q\ne r),
136:  \qquad \frac{d_-}{d_+}\geq\delta.
````

## src-a18e3e0636d090d3

`papers/tpc-286-diagonal-deletion-attachment-ledger/paper/main.tex`，原始第 130 行。

````text
128: \section{Exact diagonal split}
129: 
130: \begin{theorem}[diagonal output and physical split]
131: For every finite $I$, finite prime shell $\mathcal S_Q$, source vector $\beta$,
132: $H>0$, and integer $s\geq1$, define $g_{\full}$ and $g_{\phys}$ by
133: \eqref{eq:full}--\eqref{eq:physical}.  Then
134: \begin{equation}
135:  g_{\del}(u)=\sum_{q\in\mathcal S_Q}qK_H(0)
````

## src-a390acdf9c462b74

`papers/tpc-287-prime-shell-cancellation-depth/paper/main.tex`，原始第 135 行。

````text
133: \section{Exact shell additivity}
134: 
135: \begin{theorem}[finite component decomposition]
136: For every finite $I$ and finite prime set $\shell$, every source vector $\beta$,
137: and every fixed kernel, the outputs in \eqref{eq:component}--\eqref{eq:shell}
138: satisfy
139: \begin{equation}
140:  g_{\shell}=\sum_{q\in\shell}g_q.
````

## src-a757ab5aa420ad8b

`papers/tpc-288-growing-shell-gram-obstruction/paper/main.tex`，原始第 214 行。

````text
212: \end{proof}
213: 
214: For the aggregate physical matrix, define the active set
215: \begin{equation}
216:  \activeset=\{u\in I:q\nmid u\text{ for every }q\in\shell\}.
217:  \label{eq:active}
218: \end{equation}
219: Rows and columns outside this set vanish for every component.  A full-rank
````

## src-a8e7c6f72eb2c3d6

`papers/tpc-287-prime-shell-cancellation-depth/paper/main.tex`，原始第 206 行。

````text
204: \end{proof}
205: 
206: The envelope is intentionally conservative.  The component intervals share
207: source-weight uncertainty, and the interval for the shell sum is computed
208: directly rather than by asserting endpoint equality with the sum of component
209: intervals.  Thus a small $r^+$ is useful finite evidence of cancellation, but
210: not a limiting proportion or a norm estimate.
211: 
````

## src-df2f709579fb558f

`papers/tpc-288-growing-shell-gram-obstruction/code/tpc288_growing_shell_gram_certificate.py`，原始第 337 行。

````text
335: 
336:     gram_rank = rank_mod(gram_matrix(outputs))
337:     active_count = sum(all(value % prime for prime in shell)
338:                        for value in indices)
339:     operator_active_rank: int | None = None
340:     operator_rank_mod: int | None = None
341:     if rank_audit:
342:         operator_active_rank, operator_rank_mod = active_operator_rank(
````

## src-e780b19c0bec9033

`papers/tpc-286-diagonal-deletion-attachment-ledger/code/tpc286_diagonal_deletion_attachment_certificate.py`，原始第 257 行。

````text
255:     need(parent_c == frozen_c,
256:          "TPC284 source interval mismatch")
257:     reconstructed = (c_full[0] - c_diag[1], c_full[1] - c_diag[0])
258:     need(reconstructed[0] <= c_phys[0] and reconstructed[1] >= c_phys[1],
259:          "component reconstruction does not contain physical interval")
260:     full_sign, diag_sign, phys_sign = sign(c_full), sign(c_diag), sign(c_phys)
261:     ratio_lower = abs_lower(c_diag) / abs_upper(c_phys)
262:     return {
````

## src-f1b58736ac9ecc21

`papers/tpc-288-growing-shell-gram-obstruction/paper/main.tex`，原始第 164 行。

````text
162: \end{equation}
163: 
164: \begin{lemma}[Gram positivity and energy decomposition]
165: The matrix $G$ is real symmetric positive semidefinite.  If $\one_{\shell}$
166: is the all-ones vector, then
167: \begin{equation}
168:  \operatorname{tr}G=\sum_{q\in\shell}\|g_q\|_2^2=:E_{\mathrm{diag}},
169:  \qquad
````

## src-f8e962f7128fa9ba

`papers/tpc-286-diagonal-deletion-attachment-ledger/PROOF_PACKAGE.md`，原始第 122 行。

````text
120: $$
121: 
122: The four-block projected attachment is linear in $g$ because each block sum
123: and each contrast sum is linear, while the interval-valued source weights are
124: fixed during the evaluation.  Thus it satisfies the required hypothesis.
125: 
126: Therefore the exact operator and attachment decompositions follow. $\square$
127: 
````

## src-fea9c5a4bbbd936e

`papers/tpc-285-prime-shell-residue-rank-obstruction/paper/main.tex`，原始第 189 行。

````text
187: \end{table}
188: 
189: For the last two columns we reduce integer-scaled residue matrices and the
190: rational kernel matrix modulo $p=1{,}000{,}000{,}007$.  Every denominator
191: $H^2+(u-t)^2$ is nonzero modulo $p$.  A full-rank reduction gives a nonzero
192: rational minor, so the rational matrix has full active rank.  The certificate
193: checks this independently for all 20 rows:
194: \begin{equation}
````
