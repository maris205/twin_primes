---
type: "source-locator"
generated: true
---


# DOC-4d54663121ccbfdb 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-00fac7b547c8992d

`papers/tpc-333-source-polarization-cross-term/paper/main.tex`，原始第 88 行。

````text
86: \section{Polarization ledger}
87: 
88: For finite real vectors $a,b$, symmetry and bilinearity of the Euclidean
89: inner product give
90: \begin{equation}\label{eq:polarization}
91:  \|a-b\|_2^2=\langle a-b,a-b\rangle
92:  =\|a\|_2^2+\|b\|_2^2-2\langle a,b\rangle.
93: \end{equation}
````

## src-061b262047151f79

`papers/tpc-330-multi-permutation-response-spectrum/paper/main.tex`，原始第 97 行。

````text
95: and a half split in increasing prime order.
96: 
97: For a finite vector $v=(v_t)_{t\in I_{o,N}}$, define
98: \begin{align}
99:  E_e(v)&=\|C_ev\|_2^2,\\
100:  D_e(v)&=\sum_t v_t^2\|C_ee_t\|_2^2,\\
101:  O_e(v)&=E_e(v)-D_e(v),\qquad
102:  R_e(v)=\frac{E_e(v)}{D_e(v)}.
````

## src-06395d356cabcc23

`papers/tpc-331-control-average-centered-response-decomposition/paper/main.tex`，原始第 118 行。

````text
116: \[
117:  \pi_{7,29}(i)=(7i+29)\bmod M,\qquad
118:  \pi_{\rm rev}(i)=M-1-i,qquad M=N/2.
119: \]
120: The odd affine multipliers are units modulo the powers of two $M=2048,4096$.
121: Consequently, each associated permutation matrix $P_j$ preserves the source
122: multiset and Euclidean norm exactly.  Put
123: \[
````

## src-1b7b65a17152a91e

`papers/tpc-330-multi-permutation-response-spectrum/paper/main.tex`，原始第 151 行。

````text
149: \section{Exact identities and certificate protocol}
150: 
151: \paragraph{Finite Gram identity.}
152: Since $C_ev=\sum_t v_tC_ee_t$, finite bilinearity gives
153: \[
154:  E_e(v)=\sum_{t,t'}v_tv_{t'}
155:        \langle C_ee_t,C_ee_{t'}\rangle.
156: \]
````

## src-216695bf1fac5461

`papers/tpc-333-source-polarization-cross-term/paper/main.tex`，原始第 112 行。

````text
110: \section{Protocol and exact anchor}
111: 
112: The producer evaluates the source arrays for the six pairs $(o,N)$, records
113: the four terms in \eqref{eq:polarization}, and compares the two nested scales
114: at each origin.  It also stores nonzero-coordinate and coordinate-sign
115: counts, so that a later support audit can use the same rows.  The independent
116: checker uses its own trial sieve, reverse distinct-factorization pass, and
117: reverse order for the finite tail product.  It does not import the producer's
````

## src-2258f5f36c40c38c

`papers/tpc-333-source-polarization-cross-term/paper/main.tex`，原始第 183 行。

````text
181: \section{What the ledger does and does not prove}
182: 
183: The strongest positive result is a clean source-level interface: the four
184: terms, dimensionless coefficient, and nested-scale comparisons are all
185: recomputed independently on six disjoint-from-parent windows.  The strongest
186: obstruction is equally clear: finite source polarization is in a mixed
187: regime, so neither near orthogonality nor near total cancellation is a safe
188: replacement for a future uniform estimate.
````

## src-22899e7546776d6b

`papers/tpc-330-multi-permutation-response-spectrum/paper/main.tex`，原始第 128 行。

````text
126: guard $5\cdot10^{-8}$.
127: 
128: Let $P_j$ be the permutation matrix associated with one of the five maps.
129: Because $M$ is either $2048$ or $4096$, the multipliers $1,3,5,7$ are units
130: modulo $M$.  Hence
131: \[
132:  P_j^{T}P_j=I,\qquad
133:  \|P_jv\|_2=\|v\|_2,\qquad
````

## src-27d9d788f9b3f6be

`papers/tpc-334-cross-term-support-ledger/paper/main.tex`，原始第 67 行。

````text
65: TPC-333.  All shifted values $t+2$ in this paper remain below that cutoff.
66: 
67: The cross term is the finite sum
68: \[
69:  X_o(N)=\langle\Lambda,b\rangle
70:        =\sum_{t\in I_{o,N}}\Lambda(t+2)b_o^{(2)}(t).
71: \]
72: All summands are nonnegative in this model.  The producer records each class
````

## src-2a6a52094bebee0a

`papers/tpc-331-control-average-centered-response-decomposition/PROOF_PACKAGE.md`，原始第 3 行。

````text
1: # TPC-331 proof and scope package
2: 
3: ## Proposition 1: control-orbit Pythagorean identity
4: 
5: Let `A` be any real symmetric matrix, let `w_1,...,w_m` be finite vectors,
6: let `v_bar=m^{-1}sum_j w_j`, and let `z_j=w_j-v_bar`.  Then
7: 
8: ```text
````

## src-40408570b793f2c1

`papers/tpc-332-growing-control-average-ensemble/PROOF_PACKAGE.md`，原始第 16 行。

````text
14: `mean_j z_j=0` to cancel the cross term.  ∎
15: 
16: ## Proposition 2 — signed-Gram specialization
17: 
18: Taking `A=C_e` gives the energy identity.  Taking the diagonal matrix whose
19: `t`-th entry is `sum_u C_e(u,t)^2` gives the coordinate-diagonal identity.
20: Subtracting the latter from the former gives the off-diagonal identity.  All
21: three statements are exact finite algebra.
````

## src-89b16d74477d7204

`papers/tpc-331-control-average-centered-response-decomposition/paper/main.tex`，原始第 123 行。

````text
121: Consequently, each associated permutation matrix $P_j$ preserves the source
122: multiset and Euclidean norm exactly.  Put
123: \[
124:  w_j=P_jv,\qquad \bar v=\frac15\sum_{j=1}^5w_j,
125:  \qquad z_j=w_j-\bar v.
126: \]
127: Then $\sum_jz_j=0$.
128: 
````

## src-a5c9234a951915a5

`papers/tpc-333-source-polarization-cross-term/paper/main.tex`，原始第 102 行。

````text
100: Then, exactly,
101: \begin{equation}\label{eq:complement}
102:  \rho=1-\kappa,qquad
103:  \operatorname{corr}(\Lambda,b)=
104:  \frac{\langle\Lambda,b\rangle}{\|\Lambda\|_2\|b\|_2}.
105: \end{equation}
106: The coefficient $\kappa$ is a dimensionless diagnostic.  It is not a
107: positive-definite correlation coefficient and need not lie in $[0,1]$ in an
````

## src-a7afd109ec9f67d7

`papers/tpc-332-growing-control-average-ensemble/paper/main.tex`，原始第 49 行。

````text
47: 
48: \section{Declared finite model}
49: For an origin $o$ and even scale $N$, set
50: \[
51:  I_{o,N}=\{o,o+1,\ldots,o+N/2-1\}.
52: \]
53: The new panel is
54: \[
````

## src-ba7b3d6d3a439a4b

`papers/tpc-333-source-polarization-cross-term/paper/main.tex`，原始第 96 行。

````text
94: Applying this to $a=\Lambda$ and $b=b_o^{(2)}$ gives the source identity.  Let
95: \[
96:  S=\|\Lambda\|_2^2+\|b\|_2^2>0,qquad
97:  \kappa=\frac{2\langle\Lambda,b\rangle}{S},qquad
98:  \rho=\frac{\|\Lambda-b\|_2^2}{S}.
99: \]
100: Then, exactly,
101: \begin{equation}\label{eq:complement}
````

## src-c932c0b29e718ba1

`papers/tpc-332-growing-control-average-ensemble/paper/main.tex`，原始第 94 行。

````text
92:  \pi_{7,29}(i)=7i+29\pmod M,\qquad \pi_{\rm rev}(i)=M-1-i.
93: \]
94: The odd multipliers are units modulo $M$, hence each map is a permutation.
95: Writing $P_j$ for its permutation matrix, put
96: \[
97:  w_j=P_jv,\qquad \bar v=\frac15\sum_{j=1}^5w_j,
98:  \qquad z_j=w_j-\bar v.
99: \]
````

## src-db1f6361b6f05411

`papers/tpc-332-growing-control-average-ensemble/paper/main.tex`，原始第 107 行。

````text
105: Expanding $Aw_j=A\bar v+Az_j$ cancels the cross terms, so this is an exact
106: finite identity with no limiting or arithmetic input.  If
107: \[
108:  \Delta_e=\operatorname{diag}\left(\sum_uC_e(u,t)^2\right)_t,
109:  \qquad D_e(x)=x^T\Delta_ex,
110: \]
111: the same expansion for $C_e$ and $\Delta_e^{1/2}$ gives
112: \begin{align}
````
