---
type: "source-locator"
generated: true
---


# DOC-7eeeef2a49a00287 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-00fbe01d112393a1

`papers/tpc-223-conditional-signed-reassembly-compiler/paper/main.tex`，原始第 63 行。

````text
61: \section{The conditional two-channel interface}
62: 
63: Let $E_0$ be a declared baseline exponent.  Write $A_x$ for the prime-AP and
64: collision channel, $P_x$ for the polarized four-packet cross-correlation
65: channel, and $S_x$ for the target shell quantity.  The input interface is
66: 
67: \begin{align}
68:  A_x &\ll x^{E_0-\delta_{\rm AP}+o(1)}, \label{eq:interface}\\
````

## src-0307a115d67ca775

`papers/tpc-221-collision-graph-schur-envelope/paper/main.tex`，原始第 93 行。

````text
91: \end{proof}
92: 
93: \begin{theorem}[Weighted Schur envelope]
94: Let $p_q>0$ be arbitrary.  Then
95: \[
96:  \lambda^{*}\G_h\lambda
97:  \leq \rho_h(p)\,\|\lambda\|_2^2,
98:  \qquad
````

## src-04695ec8209dcb2d

`papers/tpc-224-literal-two-channel-compatibility-audit/paper/main.tex`，原始第 97 行。

````text
95: \section{The common literal coefficient family}
96: 
97: We use the row notation inherited from TPC-220.  For a modulus $h$, a prime
98: $q$ coprime to $h$, a packet profile $\psi_j$, and a residue $a\pmod h$,
99: define
100: \begin{equation}
101:  B_{h,q}^{(j)}(a)=
102:  \sum_{0<|m|\leq \lfloor hq/H\rfloor}
````

## src-0745402d23854e4e

`papers/tpc-224-literal-two-channel-compatibility-audit/PROOF_PACKAGE.md`，原始第 44 行。

````text
42: is not included in the theorem.
43: 
44: ## Assumptions
45: 
46: - The vectors are in one common Hilbert space and use one common normalization.
47: - `P,J` are positive integers.
48: - All sums are finite, so rearrangement of the two label sums is exact.
49: 
````

## src-227f111c2b295797

`papers/tpc-223-conditional-signed-reassembly-compiler/paper/main.tex`，原始第 68 行。

````text
66: 
67: \begin{align}
68:  A_x &\ll x^{E_0-\delta_{\rm AP}+o(1)}, \label{eq:interface}\\
69:  P_x &\ll x^{E_0-\kappa_{\rm pol}+o(1)}, \\
70:  S_x &\ll x^{\lambda_{\rm struct}}(A_x+P_x).
71: \end{align}
72: 
73: Here $\delta_{\rm AP},\kappa_{\rm pol},\lambda_{\rm struct}\geq 0$ are
````

## src-32a6bb6f6c0b8f14

`papers/tpc-220-prime-ap-collision-crosswalk/paper/main.tex`，原始第 47 行。

````text
45: This paper makes that translation without changing the source object.
46: 
47: Fix an active denominator $h$, a prime $q\in\Qx$ with $(q,h)=1$, and write
48: \[
49:  L_{h,q}=\left\lfloor\frac{hq}{H}\right\rfloor,
50:  \qquad
51:  \M_{h,q}^{*}=\{m\in\mathbb Z:0<|m|\leq L_{h,q},\ (m,h)=1\}.
52: \]
````

## src-4b39449d11f4a6ed

`papers/tpc-223-conditional-signed-reassembly-compiler/PROOF_PACKAGE.md`，原始第 5 行。

````text
3: ## Conditional compiler theorem
4: 
5: Assume a baseline exponent `E0`, nonnegative savings `delta_AP` and `kappa_pol`,
6: and a nonnegative structural loss `lambda_struct`.  Suppose the literal shell
7: quantity admits the conditional two-channel interface
8: 
9: ```text
10: A_x << x^(E0-delta_AP+o(1)),
````

## src-7200932cc4728cdb

`papers/tpc-220-prime-ap-collision-crosswalk/paper/main.tex`，原始第 108 行。

````text
106: We refer to this matrix as the \emph{Gamma} matrix below.
107: 
108: \begin{theorem}[Collision formula]
109: The Gram entry equals
110: \begin{align*}
111:  \Gamma_h^{(j,\ell)}(q,q')
112:   ={}&\sum_{m\in\M_{h,q}^{*}}
113:        \sum_{m'\in\M_{h,q'}^{*}}
````

## src-7778f3fa68415b98

`papers/tpc-221-collision-graph-schur-envelope/paper/main.tex`，原始第 75 行。

````text
73: \section{Exact PSD energy and Schur control}
74: 
75: \begin{theorem}[PSD identity]
76: The matrix $\G_h=(\G_h(q,q'))_{q,q'\in\mathcal Q}$ is Hermitian positive semidefinite.
77: For every complex weight vector $\lambda=(\lambda_q)_{q\in\mathcal Q}$,
78: \[
79:  \sum_{\substack{a\pmod h\\(a,h)=1}}
80:  \left|\sum_{q\in\mathcal Q}\lambda_q B_{h,q}(a)\right|^2
````

## src-819ccfa887ccd5fc

`papers/tpc-224-literal-two-channel-compatibility-audit/paper/main.tex`，原始第 132 行。

````text
130: \section{Sharp common-vector theorem}
131: 
132: \begin{theorem}[common two-channel compatibility]
133: \label{thm:compatibility}
134: For any finite $\Qset$ of size $P$, any positive integer $J$, and any vectors
135: $W_{q,j}$ in a common complex Hilbert space, the energies
136: \eqref{eq:ap}--\eqref{eq:all} satisfy
137: \begin{equation}
````

## src-83e0224269ba45f3

`papers/tpc-224-literal-two-channel-compatibility-audit/paper/main.tex`，原始第 230 行。

````text
228: \end{table}
229: 
230: The stress clock realizes the aligned family in the theorem.  Since the cutoff
231: is one and $q^{-1}=1\pmod5$, every active row has the same two primitive
232: coordinates.  Consequently the sharp ratio is exactly one after dividing by
233: $PJ/(P+J)$, while the unit ratio is the sharp constant itself.
234: 
235: \begin{table}[t]
````

## src-8b4502b25db23e9b

`papers/tpc-222-four-packet-cross-term-obstruction/paper/main.tex`，原始第 70 行。

````text
68: \section{Exact four-point polarization}
69: 
70: \begin{theorem}[Four-point polarization]
71: For all vectors $x,y$,
72: \[
73:  \langle x,y\rangle
74:  =\frac14\sum_{r=0}^3 i^{-r}\,\|x+i^r y\|^2.
75:  \tag{3}
````

## src-9805cf797dc5f77e

`papers/tpc-224-literal-two-channel-compatibility-audit/paper/main.tex`，原始第 189 行。

````text
187: \section{Literal growth audit}
188: 
189: The exact certificate has two named experiments.  The first is a finite
190: source-surrogate clock with actual primes in $(Q,2Q]$, $x=Q^3$,
191: $H=4Q^2$, and $h=4Q$.  It uses affine profiles
192: \[
193:  \psi_j(t)=1+\frac{\alpha_j}{10}t,
194:  \qquad (\alpha_0,\alpha_1,\alpha_2,\alpha_3)=(0,1,-1,2).
````

## src-986e831199aec4a7

`papers/tpc-224-literal-two-channel-compatibility-audit/README.md`，原始第 19 行。

````text
17: ```
18: 
19: 则 exact Cauchy 与 scalar min-to-sum identity 给出
20: 
21: ```text
22: E_all <= min(J E_AP, P E_pol)
23:        <= P J/(P+J) (E_AP+E_pol).
24: ```
````

## src-b5bce5885e5af139

`papers/tpc-222-four-packet-cross-term-obstruction/PROOF_PACKAGE.md`，原始第 18 行。

````text
16: This is an exact identity, not an estimate.
17: 
18: ## Theorem 3: trace envelope and scoped non-identifiability
19: 
20: `0<=c^*Gc<=tr(G)||c||^2`. The upper endpoint is attained by a rank-one aligned Gram.
21: The two exact fixtures `s^+` and `s^-` have identical diagonal/trace but target energies
22: `16` and `0`; hence diagonal/trace information alone cannot certify signed reassembly.
23: 
````

## src-ca6c023e4010fdf6

`papers/tpc-224-literal-two-channel-compatibility-audit/PROOF_PACKAGE.md`，原始第 55 行。

````text
53: 
54: $$
55:  V_j=\sum_qW_{q,j},\qquad U_q=\sum_jW_{q,j},qquad
56:  Z=\sum_{q,j}W_{q,j}.
57: $$
58: 
59: Then `Z=sum_j V_j=sum_q U_q`.
60: 
````

## src-cb0e5963bb8e1706

`papers/tpc-222-four-packet-cross-term-obstruction/paper/main.tex`，原始第 22 行。

````text
20: The prime-shell route carries four packet coordinates whose signed reassembly is not
21: determined by their separate energies.  We isolate this interface in exact Hilbert-space
22: form.  The four-packet Gram is positive semidefinite, its coefficient energy is a Rayleigh
23: quotient, and a four-point polarization identity reconstructs every cross-term from four
24: phase-labelled energies.  A trace bound gives a sharp universal envelope.  We then give two
25: rank-one packet fixtures with identical diagonal and trace data but target signed energies
26: $16$ and $0$.  Thus PSD and trace information alone cannot certify signed reassembly.  The
27: result is a structural obstruction and a precise specification of the missing polarized
````

## src-d125a2adbcc85d83

`papers/tpc-220-prime-ap-collision-crosswalk/paper/main.tex`，原始第 68 行。

````text
66: \section{Exact weighted prime-AP crosswalk}
67: 
68: \begin{theorem}[Prime-AP crosswalk]
69: For complex weights $(\lambda_q)_{q\in\Qx}$ and primitive $a\pmod h$, define
70: \[
71:  \Pi_{h,m}^{(j)}(r;\lambda)=
72:  \sum_{\substack{q\in\Qx, q\equiv r\ (h)\\ |m|\leq L_{h,q}}}
73:  \lambda_q w_{h,m,q}^{(j)}.
````

## src-d3e5354aad896c03

`papers/tpc-222-four-packet-cross-term-obstruction/paper/main.tex`，原始第 36 行。

````text
34: \section{Four packet interface}
35: 
36: Let $V_0,V_1,V_2,V_3$ be vectors in a complex Hilbert space.  We use the convention
37: \[
38:  \langle x,y\rangle=\sum_k\overline{x_k}y_k,
39:  \qquad
40:  \G_{j\ell}=\langle V_j,V_\ell\rangle.
41:  \tag{1}
````

## src-da80f7ed9786c386

`papers/tpc-222-four-packet-cross-term-obstruction/paper/main.tex`，原始第 94 行。

````text
92: cross-term.
93: 
94: \begin{corollary}[Trace envelope]
95: For every coefficient vector $c$,
96: \[
97:  0\leq c^*\G c\leq \operatorname{tr}(\G)\,\|c\|_2^2.
98:  \tag{4}
99: \]
````

## src-dc3921cc8b399f6b

`papers/tpc-224-literal-two-channel-compatibility-audit/paper/main.tex`，原始第 203 行。

````text
201: All row values, vector additions, and energies are computed as fractions.  The
202: independent checker reconstructs the rows without importing the producer.
203: Table~\ref{tab:source} reports the source-surrogate unit ratio
204: $\Eall/(\Eap+\Epol)$; every sharp-interface residual is exactly zero or
205: nonnegative as required.
206: 
207: \begin{table}[t]
208: \centering
````

## src-def18734ea8f9be7

`papers/tpc-223-conditional-signed-reassembly-compiler/paper/main.tex`，原始第 87 行。

````text
85: \section{Exact compiler theorem}
86: 
87: \begin{theorem}[conditional signed-reassembly compiler]
88: Assume \eqref{eq:interface}.  Define
89: \[
90:  \sigma:=\min(\delta_{\rm AP},\kappa_{\rm pol})-\lambda_{\rm struct}.
91: \]
92: Then
````

## src-e7333f9783d9d4ab

`papers/tpc-221-collision-graph-schur-envelope/paper/main.tex`，原始第 57 行。

````text
55: $a\pmod h$ with $(a,h)=1$.  Define
56: \[
57:  \G_h(q,q')=\sum_{\substack{a\pmod h\\(a,h)=1}}
58:  B_{h,q}(a)\overline{B_{h,q'}(a)}.
59:  \tag{2}
60: \]
61: The TPC-220 crosswalk gives the literal expansion
62: \[
````
