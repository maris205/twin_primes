---
type: "source-locator"
generated: true
---


# DOC-efcc407d730beef0 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-05b4e9c9e9c26ca6

`papers/tpc-210-poisson-profile-realizability/paper/main.tex`，原始第 201 行。

````text
199:  \tag{4.1}
200: \]
201: Take any centered vector $z\in\one^\perp$ and define
202: \[
203:  B_D=\mu(D)U_D^*z.
204:  \tag{4.2}
205: \]
206: Theorem~\ref{thm:interpolation} realizes every $B_D$ by a valid Schwartz
````

## src-061b0e87725863f7

`papers/tpc-212-truncated-boundary-emitter/paper/main.tex`，原始第 318 行。

````text
316: \begin{lemma}[reciprocal collision identity]
317: \label{lem:collision}
318: Let $a\equiv1$ on $I_d$ and write $N_d=E_d a$.  Then
319: \begin{equation}
320:  \norm{N_d}_2^2
321:  =\sum_{(q_1,m_1),(q_2,m_2)\in I_d}
322:  \mathbf 1_{d\mid m_1q_2-m_2q_1}.
323:  \label{eq:collision}
````

## src-0f42769da4b6c1da

`papers/tpc-210-poisson-profile-realizability/paper/main.tex`，原始第 177 行。

````text
175: \begin{proof}
176: The support of the $s$-th summand in (3.2) is contained in
177: $(n_s/q-\rho_q,n_s/q+\rho_q)$.  Since $2\rho_q<1$ and the points $n_s/q$
178: are separated by more than $10$, these intervals are disjoint and no interval
179: contains any other point of the lattice $\{n/q:n\in\Z\}$.  At the lattice
180: point $n_t/q$, the $t$-th summand has value $b(t)$ and all other summands
181: vanish.  Every other point $n/q$ in the same residue class is outside the
182: support of every summand.  Therefore the residue sum in (3.3) has exactly one
````

## src-0fc4f160007a798a

`papers/tpc-210-poisson-profile-realizability/paper/main.tex`，原始第 249 行。

````text
247:  V_D=P_qU_DB_D,
248:  \qquad
249:  G_{D,E}=\ip{V_D}{V_E}.
250:  \tag{5.1}
251: \]
252: 
253: \begin{proposition}[Gram reduction]
254: \label{prop:gram}
````

## src-11944c916f51764d

`papers/tpc-214-mobius-frequency-clusters/paper/main.tex`，原始第 223 行。

````text
221: coefficient is restored.  It is the expansion of the cluster sum:
222: \begin{equation}
223:  L\sum_{d,e\in\Dd}c_dc_e
224:  \sum_{\substack{r\bmod d,\ s\bmod e\\r/d\equiv s/e\pmod 1}}
225:  B_d(r)B_e(s)
226:  =\text{right-hand side of \eqref{eq:cluster}}.
227:  \label{eq:pairwise-expansion}
228: \end{equation}
````

## src-1f5084b7009f1451

`papers/tpc-213-physical-profile-cross-gram/paper/main.tex`，原始第 126 行。

````text
124: \subsection{Residue lifts and transforms}
125: 
126: Let $\Dd$ be a finite family of positive moduli and let $\UU$ be a finite set
127: of integers.  For a source vector $f=(f(u))_{u\in\UU}$ define the residue lift
128: \begin{equation}
129:  (C_df)(a)=\sum_{\substack{u\in\UU\\u\equiv a\pmod d}} f(u),
130:  \qquad a\in\ZZ/d\ZZ.
131:  \label{eq:lift}
````

## src-2630a3613077d295

`papers/tpc-210-poisson-profile-realizability/paper/main.tex`，原始第 149 行。

````text
147:  \tag{3.1}
148: \]
149: The points $n_s/q$ are separated from one another by more than $10$, while
150: two distinct points in the same residue class are separated by exactly one.
151: Let $\eta\in C_c^\infty((-1,1))$ satisfy $\eta(0)=1$.
152: 
153: \begin{theorem}[finite profile interpolation]
154: \label{thm:interpolation}
````

## src-2f642d5d0d83e872

`papers/tpc-212-truncated-boundary-emitter/paper/main.tex`，原始第 491 行。

````text
489: form
490: \begin{equation}
491:  \left|\sum_{d\in\Aset_{Y,U}(t)}
492:  \frac{\muM(d)\log d}{d}
493:  \ip{E_d\psi_d}{\widehat{\mathcal R}_d}\right|
494:  \leq \text{a saving bound for the coupled family},
495:  \label{eq:needed-physical-theorem}
496: \end{equation}
````

## src-302a68113e2fa5a4

`papers/tpc-211-product-coupled-euler-gram/paper/main.tex`，原始第 155 行。

````text
153: assembled one modulus at a time:
154: \[
155:  \mathcal R_d(a)=
156:  \sum_{\substack{u\in I_x\\u\equiv a\pmod d}}
157:  \frac{w(u)-\DeltaP_d(a)}{\log u},
158:  \qquad
159:  w(u)=\Lambda(u+2)-b_x^{(z)}(u).
160:  \tag{2.6}
````

## src-52dc32f8374cf2ba

`papers/tpc-210-poisson-profile-realizability/paper/main.tex`，原始第 107 行。

````text
105: \end{itemize}
106: 
107: \section{The profile interface}
108: 
109: Let $q>2$ be prime and write
110: \[
111:  \Gq=\Fq^\times,\qquad N=q-1,qquad
112:  P_q=I_N-\frac1N\one\one^*.
````

## src-5aded032fa36dae7

`papers/tpc-213-physical-profile-cross-gram/PROOF_PACKAGE.md`，原始第 112 行。

````text
110: ```
111: 
112: Summing over `u=0,...,L-1` gives a finite geometric series.  The ratio is one
113: exactly when `r/d-s/e` is an integer, and otherwise the ratio is a nontrivial
114: `L`-th root of unity because `L(r/d-s/e)` is an integer.  Consequently the
115: sum is `L` in the first case and zero in the second.  Interchanging the finite
116: sums proves
117: 
````

## src-5b9a167682d92e7c

`papers/tpc-214-mobius-frequency-clusters/README.md`，原始第 89 行。

````text
87: ```
88: 
89: The finite emitter uses the exact rational Schwartz profile
90: `psi(t)=(1+t^2)^(-2)`.  The logarithms are retained in the coefficient ledger;
91: finite energy ratios are reported with high-precision decimal evaluation.
92: 
93: ## Interpretation
94: 
````

## src-5ff0b85e0f75aad4

`papers/tpc-211-product-coupled-euler-gram/paper/main.tex`，原始第 109 行。

````text
107: \section{The literal product-coupled profile family}
108: 
109: Fix distinct odd primes
110: \[
111:  \mathcal P=\{p_1,\ldots,p_s\},\qquad z< p_1,\qquad
112:  M=\prod_{p\in\mathcal P}p.
113:  \tag{2.1}
114: \]
````

## src-63188d262155ab4c

`papers/tpc-212-truncated-boundary-emitter/paper/main.tex`，原始第 145 行。

````text
143: \subsection{Notation}
144: 
145: Let
146: \[
147:  \PP=\{p_1,\ldots,p_s\},\qquad p_i>2,
148: \]
149: be a finite set of distinct active primes.  For a nonempty subset
150: $S\subseteq\PP$, put
````

## src-69560959c4f389e8

`papers/tpc-212-truncated-boundary-emitter/README.md`，原始第 26 行。

````text
24: 
25: ```text
26: E_d(q,m -> r) = 1_{r = m q^{-1} (mod d)}.
27: ```
28: 
29: The exact occupancy Gram identity is
30: 
31: ```text
````

## src-6b6d3c8ce9afcbc9

`papers/tpc-214-mobius-frequency-clusters/paper/main.tex`，原始第 347 行。

````text
345: $Y_0<d\le U$.  It also does not perform the prime-only shell reassembly or
346: attach a source-backed collective BDH theorem to the four polarized packets.
347: The finite profile is one explicit Schwartz choice, not the proof of an
348: asymptotic profile law.  Accordingly, the release earns structural route
349: advance only: no arithmetic $L^2$ credit, fixed-atom credit, strict
350: $1/400$ payment, or twin-prime conclusion is claimed.
351: 
352: \section{Conclusion}
````

## src-7a731a3d652da58a

`papers/tpc-211-product-coupled-euler-gram/paper/main.tex`，原始第 469 行。

````text
467: \end{theorem}
468: 
469: \begin{proof}
470: Positive definiteness of $G$ gives a unique coefficient vector $\alpha$ with
471: $G\alpha=y$.  Taking $w=\sum_T\alpha_T\DeltaP_T$ gives (6.2), up to the
472: choice of the harmless inner-product convention.  For $y_S=\muM(d_S)$,
473: equation (6.3) is one for every $S$, and (6.4) follows by direct summation.
474: \end{proof}
````

## src-7ee0da56263af54d

`papers/tpc-210-poisson-profile-realizability/paper/main.tex`，原始第 111 行。

````text
109: Let $q>2$ be prime and write
110: \[
111:  \Gq=\Fq^\times,\qquad N=q-1,qquad
112:  P_q=I_N-\frac1N\one\one^*.
113:  \tag{2.1}
114: \]
115: For a Schwartz function $F_D$ on $\mathbb R$ and a unit divisor $D$ modulo
116: $q$, define the Poisson residue profile
````

## src-8d0040a31f869285

`papers/tpc-212-truncated-boundary-emitter/paper/main.tex`，原始第 313 行。

````text
311:  a(q,m)=\psi\!\left(\frac{Hm}{dq}\right),
312: \]
313: followed by the nonzero scalar $\muM(d)\log(d)/d$.  We first isolate the
314: pushforward algebra.
315: 
316: \begin{lemma}[reciprocal collision identity]
317: \label{lem:collision}
318: Let $a\equiv1$ on $I_d$ and write $N_d=E_d a$.  Then
````

## src-8e51bea4fe44b4cb

`papers/tpc-214-mobius-frequency-clusters/paper/main.tex`，原始第 162 行。

````text
160: \begin{corollary}[zero axis]
161: \label{cor:zero}
162: If every $q\in\QQ$ satisfies $q<H$, then $B_d(0)=0$ for every $d$.  Hence the
163: reduced denominator $h=1$ contributes no physical Gram energy.
164: \end{corollary}
165: 
166: \begin{proof}
167: The congruence for $r=0$ requires $d\mid m$.  But every nonzero admissible
````

## src-8f44ff22a800dd27

`papers/tpc-210-poisson-profile-realizability/paper/main.tex`，原始第 288 行。

````text
286: of $G$ after all TPC normalizations are restored.
287: 
288: The same point can be expressed in multiplicative Fourier coordinates.  If
289: $A_D(\chi)=(\M B_D)(\chi)$, then
290: \[
291:  G_{D,E}=\sum_{\chi\ne\chi_0}
292:  \chi(D)\overline{\chi(E)}A_D(\chi)\overline{A_E(\chi)}.
293:  \tag{5.5}
````

## src-9d022a34d7295d75

`papers/tpc-213-physical-profile-cross-gram/paper/references.bib`，原始第 10 行。

````text
8: @misc{WangTPC211,
9:   author       = {Liang Wang},
10:   title        = {Product-Coupled Euler Profiles and the Truncated-Boundary Handoff},
11:   year         = {2026},
12:   note         = {TPC-211 project, prime\_dynamics\_theory repository}
13: }
14: 
15: @misc{WangTPC212,
````

## src-b8b8c4dff07b158b

`papers/tpc-214-mobius-frequency-clusters/paper/main.tex`，原始第 112 行。

````text
110: \section{The literal emitter and its reduced frequencies}
111: 
112: Let $\Dd$ be a finite family of squarefree positive integers.  Let $\QQ$ be a
113: finite set of integers coprime to every member of $\Dd$, let $H\ge 1$, and let
114: $\psi$ be any function on the finite set of arguments that occur below.  Define
115: the coefficient-free reciprocal emitter
116: \begin{equation}
117:  B_d(r)=\sum_{q\in\QQ}\sum_{0<|m|\le dq/H}
````

## src-dfe8fe12ce9fe3d6

`papers/tpc-214-mobius-frequency-clusters/paper/main.tex`，原始第 186 行。

````text
184: \end{equation}
185: 
186: \begin{theorem}[reduced-denominator cluster factorization]
187: \label{thm:cluster}
188: Assume the hypotheses of Lemma~\ref{lem:dilation}.  On one complete period,
189: \begin{equation}
190:  \sum_{u=0}^{L-1}|K(u)|^2
191:  =L\sum_{h\in\mathcal H_*}|C_h|^2
````

## src-ef4184c8d68106db

`papers/tpc-213-physical-profile-cross-gram/PROOF_PACKAGE.md`，原始第 47 行。

````text
45: 2. The lift identity uses the solvability criterion for two congruences modulo
46:    `d` and `e`, followed by the number of solutions in a complete lcm period.
47: 3. The Gram identity uses the finite geometric sum
48:    `sum_(u=0)^(L-1) exp(2*pi*i*alpha*u)=L` when `alpha` is an integer and zero
49:    otherwise.
50: 
51: ## Proof
52: 
````

## src-fc55b58d8af7fbf6

`papers/tpc-212-truncated-boundary-emitter/paper/main.tex`，原始第 301 行。

````text
299:  0<|m|\leq\left\lfloor\frac{dq}{H}\right\rfloor\right\}.
300: \]
301: For unit weights, define the occupancy operator
302: \[
303:  E_d:\CC^{I_d}\longrightarrow\CC^{\ZZ/d\ZZ},
304:  \qquad
305:  (E_d a)(r)=\sum_{(q,m)\in I_d}
306:  a(q,m)\mathbf 1_{r\equiv m\overline q\pmod d}.
````
