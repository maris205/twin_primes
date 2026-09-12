---
type: "source-locator"
generated: true
---


# DOC-fcf8ff5546a31cee 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-0dd3e8d62db02d0f

`papers/tpc-304-overlapping-shell-label-transport/paper/main.tex`，原始第 71 行。

````text
69: \end{proposition}
70: 
71: \begin{proof}
72: The two possible signed inner products are $u$ and $-u$, so the maximum is
73: $|u|$.  If $m$ coordinates agree before alignment, the two possible mismatch
74: counts are $|O|-m$ and $m$; the optimal one is their minimum.  Since binary
75: labels give $u=|O|-2\min(m,|O|-m)$, division by $|O|$ yields the identity.
76: Multiplying either label by a global sign changes $u$ by at most a sign and
````

## src-138e7081c71caafe

`papers/tpc-302-growing-shell-budget-gap-audit/paper/main.tex`，原始第 93 行。

````text
91: \end{proof}
92: 
93: \begin{proposition}[Budget monotonicity and normalization]
94: Relaxing $\tau$ or enlarging a profile prefix cannot increase (1).  At a
95: common prefix, a positive target-independent source normalizer cancels from
96: the weighted/positive budget ratio.
97: \end{proposition}
98: \begin{proof}
````

## src-1605be9b9ddf7160

`papers/tpc-300-native-budget-dual-certificate/paper/main.tex`，原始第 112 行。

````text
110: it is the value of a target-space supporting functional.
111: 
112: \begin{proposition}[active strong duality]
113: If
114: \[
115:  \operatorname{dist}(b,\operatorname{range}V)<R<\norm{b}_2
116: \]
117: and $b$ has a visible component in $\operatorname{range}V$, there is a
````

## src-22dd073d02a83f5f

`papers/tpc-301-budget-gap-robustness-audit/paper/main.tex`，原始第 48 行。

````text
46: convention or by comparing two targets in different source spaces.
47: 
48: This paper isolates that vulnerability.  Let $S$ be a frozen shell, $A$ the
49: physical source-to-shell matrix, and $U_k$ the first $k$ literal cutoff
50: profiles.  Put
51: \[
52:         V_k=A^TU_k,\qquad M_k=U_k^TU_k.
53: \]
````

## src-30da145fe968d6fc

`papers/tpc-302-growing-shell-budget-gap-audit/PROOF_PACKAGE.md`，原始第 40 行。

````text
38: prefix comparison to a common-prefix comparison.
39: 
40: ## Numerical scope
41: 
42: The 34 source-first sign labels and all reported ratios are exact rational
43: replays.  The frontier values are 60-digit numerical calculations enclosed
44: outward and independently checked for the declared finite rows.  They are
45: not asymptotic estimates.  The growing profile-budget theorem, arithmetic
````

## src-31e8f69e80594972

`papers/tpc-300-native-budget-dual-certificate/paper/main.tex`，原始第 151 行。

````text
149: stationarity equation and generally misses the active residual.
150: 
151: \section{Exact rational certificate compiler}
152: 
153: For rational $V,M,b,R^2$ and rational $\rho>0$, equation (3) is a rational
154: linear system.  Exact Gaussian elimination over $\Q$ produces
155: $c_\rho\in\Q^k$, and (4) is an exact rational number.  The compiler therefore
156: stores two layers:
````

## src-33b02e610f26978a

`papers/tpc-302-growing-shell-budget-gap-audit/paper/main.tex`，原始第 40 行。

````text
38: TPC-288 growth/control grid.
39: 
40: Let $S$ be a finite prime shell and let $g_q$ be the exact literal physical
41: output vector attached to $q\in S$.  Put
42: \[
43:  G_{q,r}=\langle g_q,g_r\rangle,\qquad
44:  R(a)=\frac{a^TGa}{\operatorname{tr}G},\quad a_q\in\{\pm1\}.
45: \]
````

## src-3500e181b24b5f06

`papers/tpc-301-budget-gap-robustness-audit/paper/main.tex`，原始第 137 行。

````text
135: \section{Hostile audit protocol}
136: 
137: For each row and each $\tau\in\{1/4,1/2,3/4\}$, we compute all least-squares
138: residual ratios along the 17-profile prefix ladder.  Let $k_w(\tau)$ and
139: $k_+(\tau)$ be the first feasible indices for the weighted and positive
140: targets.  The audit checks $k_+(\tau)\leq k_w(\tau)$ and uses three contexts:
141: \begin{enumerate}
142: \item \emph{common weighted prefix}: both targets use $k_w(\tau)$;
````

## src-35256e44f01cb2c4

`papers/tpc-301-budget-gap-robustness-audit/PROOF_PACKAGE.md`，原始第 31 行。

````text
29: proves B_{k,tau}(alpha b)=alpha^2 B_{k,tau}(b).
30: 
31: ### Proposition 3 (first feasible prefix)
32: 
33: The least-squares residual is the distance from b to range(V_k).  Prefix
34: inclusion gives range(V_k) contained in range(V_l) for k <= l, so r_k(b)
35: is nonincreasing.  The set of indices satisfying r_k(b) <= tau therefore
36: has a first element, and increasing tau can only move that first element to
````

## src-59b7bed539fce0c2

`papers/tpc-304-overlapping-shell-label-transport/paper/main.tex`，原始第 85 行。

````text
83: the raw rational correlations are the primary data.
84: 
85: \section{Finite crosswalk}
86: 
87: Table~\ref{tab:crosswalk} groups the six exponent/pair rows by adjacent
88: $Q$ transition.  ``Budget desc.'' is the number of TPC-303 descents among its
89: 18 combinations of exponent, tolerance, and normalizer.  The same-prefix
90: column is the corresponding restricted count.
````

## src-5a85598fe81ea496

`papers/tpc-303-cardinality-monotonicity-obstruction/paper/main.tex`，原始第 72 行。

````text
70: \end{proof}
71: 
72: A descent with equal common prefix $k$ is especially informative: it cannot
73: be blamed on adding or removing profile directions.  It can still reflect the
74: moving physical shell or the source-first change in the signed target.
75: 
76: \section{Results}
77: 
````

## src-5eede762d7b9f5e9

`papers/tpc-300-native-budget-dual-certificate/paper/main.tex`，原始第 124 行。

````text
122: \end{proposition}
123: 
124: \begin{proof}
125: In singular coordinates of $W$, the squared residual is
126: \[
127:  \norm{b_\perp}_2^2+
128:  \sum_j\left(\frac{\rho}{\sigma_j^2+\rho}\right)^2a_j^2.
129: \]
````

## src-6e08bdc3d8d58e50

`papers/tpc-303-cardinality-monotonicity-obstruction/paper/main.tex`，原始第 52 行。

````text
50: \section{Interval certificate}
51: 
52: \begin{proposition}[Certified order]
53: If $B_j\in[L_j,U_j]$ and $B_{j+1}\in[L_{j+1},U_{j+1}]$, then
54: $U_{j+1}<L_j$ implies $B_{j+1}<B_j$, while $L_{j+1}>U_j$ implies
55: $B_{j+1}>B_j$.
56: \end{proposition}
57: \begin{proof}
````

## src-7f0d8ea613251f6e

`papers/tpc-304-overlapping-shell-label-transport/PROOF_PACKAGE.md`，原始第 15 行。

````text
13: maximal one is `|u|`.  If `m` coordinates agree before alignment, the number
14: of mismatches is `|O|-m`; after the better global sign it is the smaller of
15: these two counts.  For binary labels `u=(|O|-2d_min)`, which gives the stated
16: identity.  A global sign flip changes `u` only by a sign, leaving `|u|` and
17: the minimized mismatch count unchanged.  ∎
18: 
19: ## Proposition 2: finite crosswalk statement
20: 
````

## src-8c7dec0323c6c060

`papers/tpc-302-growing-shell-budget-gap-audit/paper/main.tex`，原始第 67 行。

````text
65: \section{Exact finite identities}
66: 
67: \begin{proposition}[Gram identity and global signs]
68: For every finite shell, $G$ is positive semidefinite and $R(a)=R(-a)$.
69: Fixing the first sign to $+1$ therefore represents every global-sign class.
70: \end{proposition}
71: \begin{proof}
72: For any coefficient vector $c$,
````

## src-99f89341c9c6214d

`papers/tpc-304-overlapping-shell-label-transport/paper/main.tex`，原始第 52 行。

````text
50: \section{Gauge-invariant transport identity}
51: 
52: For binary labels $a,b$ on a nonempty overlap $O$, define
53: \[
54:  \rho(a,b)=\max_{\varepsilon\in\{-1,+1\}}
55:        \frac{1}{|O|}\sum_{p\in O}a(p)\varepsilon b(p),
56:  \qquad
57:  d(a,b)=\min_{\varepsilon\in\{-1,+1\}}
````

## src-9ffd2f6c11a6b7d8

`papers/tpc-304-overlapping-shell-label-transport/code/tpc304_overlapping_shell_label_transport.py`，原始第 169 行。

````text
167: 
168: 
169: def transport_row(left: dict[str, Any], right: dict[str, Any],
170:                   exponent: int) -> dict[str, Any]:
171:     left_map = dict(zip(left["shell"], left["weighted_target_label"]))
172:     right_map = dict(zip(right["shell"], right["weighted_target_label"]))
173:     overlap = sorted(set(left_map) & set(right_map))
174:     need(bool(overlap), "nonempty adjacent-shell overlap")
````

## src-c1121008348e576c

`papers/tpc-303-cardinality-monotonicity-obstruction/paper/main.tex`，原始第 38 行。

````text
36: inference is stronger than the TPC-302 gap statement and needs its own test.
37: 
38: We freeze source scale $N=512$, height $H=58$, comparison cutoff $z=5$, and
39: compare the moving shells indexed by $Q=50,60,70,90$.  Their cardinalities are
40: $10,13,15,17$.  The shells are not nested; the claim under attack is therefore
41: cardinality-only monotonicity, not monotonicity under set inclusion.
42: 
43: For a common profile prefix $k$ and target $b$, TPC-302 uses
````

## src-c359a2f652a3919a

`papers/tpc-304-overlapping-shell-label-transport/paper/main.tex`，原始第 108 行。

````text
106: \end{table}
107: 
108: The middle overlap has aligned disagreement fraction $5/11$ for both
109: exponents, while the other group means are $1/2$.  Thus $60\to70$ is the
110: unique minimum of the three group means and the only group with rows below the
111: declared $1/3$ threshold.  Independently, the TPC-303 transition census is
112: $(3,15,3)$ for descents and $(0,9,0)$ for same-prefix descents.  The unique
113: minimum-correlation transition is therefore also the unique maximum-descent
````

## src-c5394a3f22864f28

`papers/tpc-300-native-budget-dual-certificate/paper/main.tex`，原始第 71 行。

````text
69: \section{Dual formula}
70: 
71: \begin{theorem}[weak native-budget dual]
72: Let $M\succ0$, let $V$ and $b$ be finite real data, let $R\geq0$, and let
73: $\rho>0$.  Define
74: \[
75:  (V^TV+\rho M)c_\rho=V^Tb.                                  \tag{3}
76: \]
````

## src-c765646099732fcc

`papers/tpc-302-growing-shell-budget-gap-audit/PROOF_PACKAGE.md`，原始第 20 行。

````text
18: finite sign domain.
19: 
20: ## Proposition 3 - budget monotonicity
21: 
22: For (0<\tau_1\leq\tau_2), the feasible ball for (\tau_1) is contained in
23: that for (\tau_2), so (B_{k,\tau_1}(b)\geq B_{k,\tau_2}(b)).  Since the
24: columns of (V_k) are nested, enlarging a prefix also enlarges the feasible
25: set and cannot increase the minimum.  The first feasible prefix is therefore
````

## src-cea5ac63e992f299

`papers/tpc-304-overlapping-shell-label-transport/paper/main.tex`，原始第 75 行。

````text
73: $|u|$.  If $m$ coordinates agree before alignment, the two possible mismatch
74: counts are $|O|-m$ and $m$; the optimal one is their minimum.  Since binary
75: labels give $u=|O|-2\min(m,|O|-m)$, division by $|O|$ yields the identity.
76: Multiplying either label by a global sign changes $u$ by at most a sign and
77: does not change its absolute value or the minimized mismatch count.
78: \end{proof}
79: 
80: The producer records the optimizing sign, all restricted labels, mismatch
````

## src-f85925897d48adf4

`papers/tpc-301-budget-gap-robustness-audit/paper/main.tex`，原始第 78 行。

````text
76: \section{Finite theorem layer}
77: 
78: \begin{proposition}[Tolerance nesting]
79: For fixed $k$ and $0<\tau_1\leq\tau_2<1$,
80: \[
81:  B_{k,\tau_1}(b)\geq B_{k,\tau_2}(b)
82: \]
83: whenever both frontiers are feasible.
````
