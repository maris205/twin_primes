---
type: "source-locator"
generated: true
---


# DOC-a8a490eeddf9cf67 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-095b4e3e84cd7fbb

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/PROOF_PACKAGE.md`，原始第 36 行。

````text
34: sign, outer `q`, and conjugated `K_H(0)`.
35: 
36: For the Poisson step, set `phi(v)=conjugate(psi_+(-v))`.  Reflection and
37: conjugation preserve compact support in `[-1,1]`, and its inverse physical
38: kernel is `conjugate(K_H(-h))`.  The V43 complete unit-centered row therefore
39: applies in the adjoint orientation.  Every nonzero dual frequency has
40: absolute profile argument at least `H/q>1` when `q<=2Q<H`; hence `P*=0`.
41: 
````

## src-0b221ffbdf41f702

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/paper/main.tex`，原始第 175 行。

````text
173: normal form, not an estimate.
174: 
175: \section{Unit-mask and normalization firewalls}
176: 
177: For $q\nmid t$, write
178: \begin{equation}
179:  c_{q,t}(u)=\one_{u\equiv t\,(q)}-\frac1{q-1},\qquad
180:  d_q(u)=\frac{\one_{q\mid u}}{q-1}.                              \label{eq:cd}
````

## src-0ce7be5decabd0f3

`papers/tpc-258-source-frozen-transverse-null-direction/paper/main.tex`，原始第 345 行。

````text
343: \]
344: 
345: \begin{theorem}[Source-frozen transverse diagonal cancellation]\label{thm:null}
346: For the unit vector \(z_{\rm null}\),
347: \[
348:  \boxed{\ip{z_{\rm null}}{\Ax\beta}=o(S_x)}.
349: \]
350: The statement is in \(\mathbb C\) and retains the TPC-255 unit, diagonal,
````

## src-0f5067de5139e7bc

`papers/tpc-257-four-block-haar-transverse-norm-floor/paper/main.tex`，原始第 188 行。

````text
186: remainder.  The three elementary integrals are summarized in Table~\ref{tab:curv}.
187: 
188: \begin{table}[ht]
189: \centering
190: \caption{Second-order curvature constants.}
191: \label{tab:curv}
192: \begin{tabular}{@{}ccccc@{}}
193: \toprule
````

## src-1f8d6a36fa4d043d

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/paper/main.tex`，原始第 58 行。

````text
56: where $\operatorname{supp}\psi_+\subset[-1,1]$ and
57: $K_H(0)=\int\psi_+=1$.  For $u,t\in I_x$, the source-frozen operator is
58: \begin{equation}
59:  \Ax(u,t)=\one_{u\ne t}\sum_{q\in\Qx}q\one_{q\nmid u}\one_{q\nmid t}
60:  K_H(u-t)\left(\one_{u\equiv t\,(q)}-\frac1{q-1}\right).        \label{eq:operator}
61: \end{equation}
62: This orientation and the associated scalar are fixed in TPC-247
63: \cite{tpc247}; the physical V59 source is \cite{v59}.
````

## src-3e4bab3f07bc80d2

`papers/tpc-258-source-frozen-transverse-null-direction/paper/main.tex`，原始第 367 行。

````text
365: \end{proof}
366: 
367: \begin{proposition}[Conditional rate refinement]\label{prop:nullrate}
368: If the two scalar formulas have remainder
369: \(O_{\psi,\e}(S_x/\log x+x^{55/48+\e})\), then
370: \[
371:  |\ip{z_{\rm null}}{\Ax\beta}|
372:  \ll_{\psi,\e}S_x/\log x+x^{55/48+\e}.
````

## src-465984fa33c2c6ee

`papers/tpc-254-source-backed-rank-midpoint-hybrid-mean-closure/paper/main.tex`，原始第 55 行。

````text
53: \end{abstract}
54: 
55: \section{Frozen objects and typed source input}
56: 
57: Fix a finite admissible $K$ and write
58: \begin{equation}
59:  Z_x=(\log x)^K,\qquad
60:  w(u)=\Lambda(u+2)-b_x^{(Z_x)}(u).                    \label{eq:residual}
````

## src-46b1bad6eb89166b

`papers/tpc-256-literal-beta-haar-adjoint-asymptotic/paper/main.tex`，原始第 117 行。

````text
115: The divisor lane requires no cancellation estimate for $\mu$.
116: 
117: \begin{lemma}[Exact layerwise density cancellation]\label{lem:divisor}
118: One has
119: \begin{equation}
120:  \left|\ip{\zm}{D_U}\right|
121:  \leq \rho U\left(\frac1\ell+\frac1r\right)
122:  =\frac{U}{\rho}=O(x^{-67/400}).                    \label{eq:divisorbound}
````

## src-475b5ffd7a894041

`papers/tpc-256-literal-beta-haar-adjoint-asymptotic/paper/main.tex`，原始第 341 行。

````text
339: uses the combined mask throughout.
340: 
341: \begin{theorem}[Diagonal-dominant adjoint phase]\label{thm:adjoint}
342: As real $x\to\infty$,
343: \begin{equation}
344:  \boxed{\displaystyle
345:  \ip{\zm}{\Ax\beta}
346:  =-\left(\frac{9\log(32/27)}{2\sqrt2}+o(1)\right)
````

## src-4fc7520f667e7d19

`papers/tpc-258-source-frozen-transverse-null-direction/README.md`，原始第 67 行。

````text
65: TPC258_NULL_DIRECTION = PROVED_SOURCE_FROZEN_UNIT_VECTOR
66: TPC258_LEADING_DIAGONAL_CANCELLATION = PROVED_SOURCE_BACKED
67: TPC258_RATE_REFINEMENT = CONDITIONAL_THEOREM_LOG_ONE_OVER_X
68: TPC258_FIXED_POWER_SAVING = NONE
69: TPC258_L2 = NONE
70: TPC258_FULL_GATE_B = OPEN
71: TPC258_FULL_GATE_B_STRICT_1_OVER_400 = UNPAID_GLOBAL
72: TPC258_FIXED_ATOM_CREDIT = 0
````

## src-503e375c4f33c693

`papers/tpc-259-same-clock-null-coupling/paper/main.tex`，原始第 287 行。

````text
285: The open residual cannot be controlled by projection algebra alone.
286: 
287: \begin{proposition}[Exact synthetic non-promotion witness]\label{prop:witness}
288: There exist a real unit vector \(z\), real vectors \(w,\beta\), and a real
289: zero-diagonal matrix \(A\) such that
290: \[
291:  \ip{z}{w}=0,\qquad
292:  \overline{\ip{z}{w}}\ip{z}{A\beta}=0,\qquad
````

## src-5abf9442e2c257a4

`papers/tpc-256-literal-beta-haar-adjoint-asymptotic/paper/main.tex`，原始第 162 行。

````text
160: \end{equation}
161: 
162: \begin{lemma}[Second-order $\Li$ curvature]\label{lem:li}
163: The ordered children satisfy
164: \begin{equation}
165:  \frac{F(m)-F(a)}{\ell}-\frac{F(b)-F(m)}r
166:  =\frac{2\log(32/27)}{\log^2x}+O\!\left(\frac1{\log^3x}\right). \label{eq:curvature}
167: \end{equation}
````

## src-5b54e1646b47695c

`papers/tpc-257-four-block-haar-transverse-norm-floor/paper/main.tex`，原始第 89 行。

````text
87:  \label{eq:rank}
88: \end{equation}
89: Split the two children in their physical order:
90: \begin{equation}
91:  s_1=\lfloor\ell/2\rfloor,\quad s_2=\ell-s_1,
92:  \qquad s_3=\lfloor r/2\rfloor,\quad s_4=r-s_3.       \label{eq:blocksizes}
93: \end{equation}
94: Let \(B_1,B_2\) be the consecutive subintervals of \(L\) of lengths
````

## src-60b5d3f085a3a645

`papers/tpc-258-source-frozen-transverse-null-direction/paper/main.tex`，原始第 323 行。

````text
321: forms in the theorem are the actual constants.
322: 
323: \section{TPC-258 source-frozen null cancellation}
324: 
325: Write \(S_x=x^{7/6}/\log^3x\), and set
326: \[
327:  L_1=\log(3456/3125),\qquad L_2=\log(884736/823543),\qquad
328:  L_T=(L_1^2+L_2^2)^{1/2},\qquad
````

## src-695134ec1315208a

`papers/tpc-254-source-backed-rank-midpoint-hybrid-mean-closure/paper/main.tex`，原始第 77 行。

````text
75: canonicality \cite{tpc253}.
76: 
77: The analytic input is the hybrid H2 theorem frozen in the local comparison
78: compiler \cite{compiler}.  For each fixed $\gamma<1/2$ and each requested
79: fixed logarithmic strength, it supplies
80: \begin{equation}
81:  \sum_{m\leq x^\gamma}\tau(m)^B\max_J
82:  \left|\sum_{\substack{x/2<ms\leq x\\s\in J}}w(ms)\right|
````

## src-6d5908ec005593b5

`papers/tpc-259-same-clock-null-coupling/paper/main.tex`，原始第 237 行。

````text
235: \end{proof}
236: 
237: \begin{theorem}[Same-clock null-channel suppression]\label{thm:channel}
238: For every fixed admissible \(K\) and every fixed \(M>0\), the first term in
239: \eqref{eq:split} satisfies
240: \begin{equation}
241:  \boxed{\displaystyle
242:  \overline{\ip{\znull}{w}}\ip{\znull}{\Ax\beta}
````

## src-84a7ec1f7980cb37

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/PROOF_PACKAGE.md`，原始第 60 行。

````text
58: ## Unit-mask proof
59: 
60: When `q` does not divide `t`, direct coordinate inspection gives
61: `v=c+d`.  Across one complete period, `c` and `d` have means
62: `-1/(q-1)` and `+1/(q-1)`.  Thus applying centered Poisson to either part
63: alone is invalid.  If `q|t`, the input mask makes the literal summand zero;
64: the unit-centered row theorem is not invoked.
65: 
````

## src-9455ba7c9b09c94d

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/paper/main.tex`，原始第 127 行。

````text
125: \eqref{eq:full}.
126: 
127: For the Poisson attachment, use the reflected-conjugate profile
128: $\phi(v)=\overline{\psi_+(-v)}$.  Reflection and conjugation preserve support
129: in $[-1,1]$, and its physical kernel is $\overline{K_H(-h)}$.  Thus the V43
130: complete-lattice theorem \cite{v43} applies in the adjoint direction without
131: assuming that $K_H$ is even or real.  When $q\leq2Q<H$, every nonzero dual
132: frequency lies outside the profile support, so $P^*_{q,t}=0$.  Finally,
````

## src-97eae9abedc607c5

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/paper/main.tex`，原始第 182 行。

````text
180:  d_q(u)=\frac{\one_{q\mid u}}{q-1}.                              \label{eq:cd}
181: \end{equation}
182: Then $v_{q,t}=c_{q,t}+d_q$, but over one period
183: \begin{equation}
184:  \sum_{u\bmod q}c_{q,t}(u)=-\frac1{q-1},\qquad
185:  \sum_{u\bmod q}d_q(u)=+\frac1{q-1}.                            \label{eq:modes}
186: \end{equation}
187: Only their sum is centered.  Their complete-lattice zero-frequency terms are
````

## src-9caf2d9cef27020c

`papers/tpc-259-same-clock-null-coupling/code/tpc259_null_coupling_certificate.py`，原始第 46 行。

````text
44: }
45: 
46: SOURCE_MARKERS = {
47:     "AGENTS.md": ("The primary agent owns repository synchronization.",
48:                    "The primary agent alone stages, commits, rebases, and pushes."),
49:     "TPC_HANDOFF.md": ("TPC258_MAXIMUM_CLAIM", "TPC258_ROUND2_CLUE"),
50:     "papers/tpc-258-source-frozen-transverse-null-direction/README.md":
51:         ("z_null=(L2 z1-L1 z2)", "TPC258_LEADING_DIAGONAL_CANCELLATION = PROVED_SOURCE_BACKED"),
````

## src-abb7dda7a619af3a

`papers/tpc-257-four-block-haar-transverse-norm-floor/paper/main.tex`，原始第 294 行。

````text
292: \end{proof}
293: 
294: \begin{corollary}[Transverse and three-mode floors]\label{cor:floors}
295: Let \(Z=\operatorname{span}\{z_0,z_1,z_2\}\) and
296: \(T=\operatorname{span}\{z_1,z_2\}\).  Then
297: \begin{align}
298:  \|P_Z\Ax\beta\|_2
299:  &=\left(\frac92\sqrt{\kappa_0^2+\kappa_1^2+\kappa_2^2}+o(1)\right)
````

## src-b3a5e586c74e66dc

`papers/tpc-256-literal-beta-haar-adjoint-asymptotic/paper/main.tex`，原始第 292 行。

````text
290: \end{proof}
291: 
292: \begin{proposition}[Boundary power separation]\label{prop:remainders}
293: For every fixed $\e>0$,
294: \begin{align}
295:  R_{\rm unit}&=O_\e(x^{5/6+\e}),                              \label{eq:unitbound}\\
296:  R_{\rm hard},R_{\rm jump}&=O_{\psi,\e}(x^{55/48+\e}).      \label{eq:boundarybound}
297: \end{align}
````

## src-b50031984915f451

`papers/tpc-259-same-clock-null-coupling/paper/main.tex`，原始第 206 行。

````text
204: \end{remark}
205: 
206: \section{Exact signed-coupling split}
207: 
208: Put
209: \begin{equation}
210:  c_x=\ip{\znull}{w},\qquad
211:  w_{\parallel}=c_x\znull,\qquad
````

## src-c05bc2347ecc0747

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/README.md`，原始第 9 行。

````text
7: ```
8: 
9: TPC-255 pushes the ordered rank-midpoint Haar vector through the literal V59
10: operator adjoint.  For every prime `q` in the frozen shell and every input
11: `t` with `q` not dividing `t`, the complete-lattice unit-centered row vanishes
12: by the V43 band-limited Poisson theorem when `H>2Q`.  Deleting the physical
13: diagonal then returns a nonzero local term; the hard endpoints of `I_x` and
14: the jump between the two rank children produce two further exact lanes.
````

## src-c34f98492f1c8228

`papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/paper/main.tex`，原始第 94 行。

````text
92: Absolute convergence follows from the Schwartz decay of $K_H$.
93: 
94: \begin{theorem}[Adjoint diagonal--boundary compiler]\label{thm:compiler}
95: For every real $x$ with $N\geq2$,
96: \begin{align}
97:  (\Ax^*\zm)(t)=\sum_{q\in\Qx}q\one_{q\nmid t}
98:  \bigg[&\zm(t)P^*_{q,t}-\zm(t)E^*_{q,t}+J^*_{q,t} \notag\\
99:  &-\frac{q-2}{q-1}\overline{K_H(0)}\zm(t)\bigg].               \label{eq:full}
````

## src-c552948146032f10

`papers/tpc-259-same-clock-null-coupling/paper/main.tex`，原始第 152 行。

````text
150: \(o(1)\) statement and is not promoted here to a fixed-power estimate.
151: 
152: \section{Four-block control of the literal hybrid residual}
153: 
154: Fix a finite admissible \(K\) and write
155: \begin{equation}
156:  Z_x=(\log x)^K,\qquad
157:  w(u)=\Lambda(u+2)-b_x^{(Z_x)}(u).                     \label{eq:w}
````

## src-c6103cf24baf832e

`papers/tpc-259-same-clock-null-coupling/paper/main.tex`，原始第 217 行。

````text
215: is purely finite-dimensional and requires no symmetry of \(A_x\).
216: 
217: \begin{proposition}[Rank-one/residual identity]\label{prop:split}
218: For every finite clock,
219: \begin{equation}
220:  \boxed{\displaystyle
221:  \ip{w}{\Ax\beta}
222:  =\overline{c_x}\ip{\znull}{\Ax\beta}
````

## src-c6cf9299bdefc1dc

`papers/tpc-257-four-block-haar-transverse-norm-floor/PROOF_PACKAGE.md`，原始第 102 行。

````text
100: ```
101: 
102: Every pair defining `z_i` consists of equal leading-width intervals.  Insert
103: this identity into each pair of means.  The two `s/d` terms cancel for each
104: fixed `d`, before summing over `d` and before applying a triangle inequality.
105: Since `|mu(d)|<=1` and `rho_i(1/p_i+1/q_i)=1/rho_i`,
106: 
107: ```text
````

## src-cf504b252f9bad24

`papers/tpc-257-four-block-haar-transverse-norm-floor/paper/main.tex`，原始第 211 行。

````text
209: for all sufficiently large real \(x\).
210: 
211: \section{Adjoint normal form for bounded variation}
212: 
213: Let \(\Qx=\{q\text{ prime}:Q<q\leq2Q\}\), and let
214: \(K_H(h)=\widehat{\psi_+}(h/H)\), with the fixed smooth compactly supported
215: profile normalized by \(\int\psi_+=1\).  The literal operator is
216: \begin{equation}
````

## src-d73b34fa8cc1a89f

`papers/tpc-256-literal-beta-haar-adjoint-asymptotic/paper/main.tex`，原始第 325 行。

````text
323: \[
324:  \frac{QH^2}{\rho}
325:  =x^{,1/3+2(21/32)-1/2+o(1)}=x^{55/48+o(1)},
326: \]
327: which proves \eqref{eq:boundarybound} after absorbing the harmless divisor
328: envelope into $x^\e$.
329: \end{proof}
330: 
````

## src-db117613ef021924

`papers/tpc-254-source-backed-rank-midpoint-hybrid-mean-closure/paper/main.tex`，原始第 122 行。

````text
120: \end{theorem}
121: 
122: \begin{proof}
123: Freeze $\gamma_0=1/4$ in \eqref{eq:h2} and choose its integer log-saving
124: parameter sufficiently strongly for the target $M$.  Every summand on the
125: left of \eqref{eq:h2} is nonnegative.  For sufficiently large $x$, the row
126: $m=1$ is present and has weight $\tau(1)^B=1$.  Hence its maximum over
127: consecutive $J\subset I_x$ is bounded by the full sum.  Applying this to the
````
