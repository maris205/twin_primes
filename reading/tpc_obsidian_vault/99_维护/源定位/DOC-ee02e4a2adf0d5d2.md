---
type: "source-locator"
generated: true
---


# DOC-ee02e4a2adf0d5d2 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-0c15d8c33ae64e4c

`papers/tpc-309-profile-prefix-shift-sensitivity/paper/main.tex`，原始第 131 行。

````text
129: \end{proof}
130: 
131: \begin{proposition}[Finite completion and ratio facts]
132: For binary $h$, enumerating subsets of at most $r$ flipped coordinates gives
133: all elements of $\mathcal C_r(h)$ exactly once.  Hence
134: \[
135:  |\mathcal C_r(h)|=\sum_{j=0}^{\min(r,m)}\binom mj,
136: \]
````

## src-1a3772fd0b3b0c8a

`papers/tpc-307-common-ambient-union-shell-holdout/paper/main.tex`，原始第 121 行。

````text
119: \end{proof}
120: 
121: \begin{proposition}[Sign and common-prefix invariances]
122: Negating a directional overlap target and its matching holdout target leaves
123: its budget and squared holdout loss unchanged.  If the two first feasible
124: prefixes are $k_L,k_R$, then $k=\max(k_L,k_R)$ is feasible for both.
125: \end{proposition}
126: \begin{proof}
````

## src-21f0ed15d808aa10

`papers/tpc-305-counterfactual-transported-label-budget/paper/main.tex`，原始第 122 行。

````text
120: \section{Finite exact statements}
121: 
122: \begin{proposition}[Alignment and extension]
123: For every nonempty overlap, (1) is a well-defined binary full-shell target and
124: maximizes the overlap inner product over the two global sign choices.  A
125: simultaneous global sign change of either parent label changes $\sigma$ so that
126: the transported vectors and all overlap mismatch counts are unchanged up to
127: the same gauge convention.
````

## src-2235675167038f7e

`papers/tpc-306-two-way-operator-target-interaction/paper/main.tex`，原始第 62 行。

````text
60: \section{Effects and exact decomposition}
61: 
62: The common intervention is the target switch left $\to$ right.  Its row-wise
63: log effects are
64: \[
65:  d_L=\log\frac{B_{LR}}{B_{LL}},\qquad
66:  d_R=\log\frac{B_{RR}}{B_{RL}}.                                  \tag{2}
67: \]
````

## src-3f27683f4b90817f

`papers/tpc-307-common-ambient-union-shell-holdout/code/tpc307_common_ambient_union_shell_holdout.py`，原始第 312 行。

````text
310: 
311: 
312: def feasible_prefix(V: mp.matrix, M: mp.matrix, target: mp.matrix,
313:                     tau: mp.mpf) -> int:
314:     target_norm_squared = squared_norm(target)
315:     need(target_norm_squared > 0, "positive overlap target norm")
316:     for k in range(1, min(V.rows, V.cols) + 1):
317:         _, residual, _ = least_squares(V[:, :k], M[:k, :k], target)
````

## src-49efcb4ada4f2166

`papers/tpc-307-common-ambient-union-shell-holdout/code/tpc307_common_ambient_union_shell_holdout.py`，原始第 296 行。

````text
294: 
295: 
296: def least_squares(V: mp.matrix, M: mp.matrix,
297:                   target: mp.matrix) -> tuple[mp.matrix, mp.mpf, mp.mpf]:
298:     coefficients = mp.qr_solve(V, target)[0]
299:     residual = V * coefficients - target
300:     residual_squared = squared_norm(residual)
301:     source_squared = (coefficients.T * M * coefficients)[0]
````

## src-57e21ec56e421c48

`papers/tpc-307-common-ambient-union-shell-holdout/paper/main.tex`，原始第 89 行。

````text
87: \]
88: 
89: For a direction $X\in\{L,R\}$ and a profile prefix of length $k$, let
90: $V_{O,k}$ be the overlap rows of $V_U$ and define the constrained source
91: budget
92: \[
93:  B_{k,\tau}(b_X)=\min_c c^\mathsf{T}M_kc\quad\text{subject to}\quad
94:  \|V_{O,k}c-b_X\|_2\leq\tau\|b_X\|_2.                           \tag{4}
````

## src-62780d80b9e17393

`papers/tpc-305-counterfactual-transported-label-budget/paper/main.tex`，原始第 65 行。

````text
63: \section{Counterfactual protocol}
64: 
65: Let $S_L,S_R$ be adjacent prime shells and let
66: $a_L:S_L\to\{-1,1\}$ and $a_R:S_R\to\{-1,1\}$ be their locked labels.  Put
67: $O=S_L\cap S_R$ and define
68: \[
69:  u=\sum_{p\in O}a_L(p)a_R(p),\qquad
70:  \sigma=\begin{cases}1,&u\geq0,\\-1,&u<0.\end{cases}
````

## src-6c9763c818df1c1b

`papers/tpc-309-profile-prefix-shift-sensitivity/paper/main.tex`，原始第 90 行。

````text
88: $V_{U,a}$, and $V_{O,a}$ is its restriction to the overlap rows.  The two
89: overlap targets are aligned by the sign of their raw binary inner product.
90: For target $t$ define $k(t,a)$ as the first ordered prefix whose
91: least-squares residual is at most $\tau^2\|t\|_2^2$.  We use the common prefix
92: \[
93:  k_a=\max\{k(t_L,a),k(t_R,a)\}.                         \tag{2}
94: \]
95: At this prefix the frontier coefficient minimizes source energy subject to
````

## src-8d005418a66bfb63

`papers/tpc-308-adversarial-exclusive-completion-envelope/paper/main.tex`，原始第 82 行。

````text
80: \section{Completion envelopes}
81: 
82: For a binary vector $h$ of length $m$ and a nonnegative integer $r$, define
83: the finite Hamming ball
84: \[
85:   \mathcal C_r(h)=\{h'\in\{-1,+1\}^m:d_H(h',h)\le r\}.
86: \]
87: If $y$ is the already fitted prediction on the same exclusive rows, define
````

## src-8d13008cc4c5a701

`papers/tpc-305-counterfactual-transported-label-budget/paper/main.tex`，原始第 129 行。

````text
127: the same gauge convention.
128: \end{proposition}
129: \begin{proof}
130: The two possible overlap inner products are $u$ and $-u$, so the displayed
131: choice of $\sigma$ selects the nonnegative one, with a deterministic choice at
132: $u=0$.  Every coordinate in (1) is a product of signs or a copied sign, hence
133: is binary.  Flipping one parent label flips $u$ and the corresponding aligned
134: neighboring label, leaving the aligned products invariant.  The off-overlap
````

## src-9793e28104e3404f

`papers/tpc-306-two-way-operator-target-interaction/paper/main.tex`，原始第 97 行。

````text
95: \end{proof}
96: 
97: \begin{proposition}[Row-normalization invariance]
98: Independent positive rescalings of the two rows of (1) leave $d_L,d_R,m,i$
99: and $q$ unchanged.
100: \end{proposition}
101: \begin{proof}
102: Multiplying both cells in one row by the same positive factor cancels in its
````

## src-987076f3d5d1f463

`papers/tpc-306-two-way-operator-target-interaction/paper/main.tex`，原始第 70 行。

````text
68: TPC-305 recorded $R_L=B_{LR}/B_{LL}$ and
69: $R_R=B_{RL}/B_{RR}$, so $d_L=\log R_L$ and $d_R=-\log R_R$.  Define
70: \[
71:  m=\frac{d_L+d_R}{2},\qquad
72:  i=\frac{d_L-d_R}{2},\qquad
73:  q=\frac{|i|}{|m|}.                                               \tag{3}
74: \]
75: The quantity $m$ measures the target-switch effect averaged over the two
````

## src-9d5e1904c8b40851

`papers/tpc-309-profile-prefix-shift-sensitivity/code/tpc309_profile_prefix_shift_sensitivity.py`，原始第 268 行。

````text
266:     left_target = mp.matrix([left_map[p] for p in overlap])
267:     right_target = mp.matrix([aligned_right[p] for p in overlap])
268:     left_k = T308.PARENT.feasible_prefix(
269:         overlap_matrix, gram, left_target, mp.mpf(tau))
270:     right_k = T308.PARENT.feasible_prefix(
271:         overlap_matrix, gram, right_target, mp.mpf(tau))
272:     k = max(left_k, right_k)
273:     left_fit = T308.PARENT.frontier(
````

## src-ae102cf4edaa9be2

`papers/tpc-309-profile-prefix-shift-sensitivity/paper/main.tex`，原始第 86 行。

````text
84: \section{Finite protocol and exact algebra}
85: 
86: For a ladder $a$, let $B_a$ be the $256\times17$ matrix of profile values and
87: $M_a=B_a^\mathsf{T}B_a$.  For a union shell $U$, the physical matrix is
88: $V_{U,a}$, and $V_{O,a}$ is its restriction to the overlap rows.  The two
89: overlap targets are aligned by the sign of their raw binary inner product.
90: For target $t$ define $k(t,a)$ as the first ordered prefix whose
91: least-squares residual is at most $\tau^2\|t\|_2^2$.  We use the common prefix
````

## src-c1c53057f5389eb5

`papers/tpc-307-common-ambient-union-shell-holdout/PROOF_PACKAGE.md`，原始第 62 行。

````text
60: is inherited from the two finite shells. `\square`
61: 
62: ## Proposition 2: global-sign invariance
63: 
64: Replacing one directional overlap target and its matching exclusive holdout
65: target by their negatives leaves its source budget and squared holdout loss
66: unchanged.
67: 
````

## src-c1ff6573a0e15321

`papers/tpc-305-counterfactual-transported-label-budget/paper/main.tex`，原始第 84 行。

````text
82: the target vector inside an operator row and does not rebuild that row.
83: 
84: For completeness, let $V_Q$ denote the finite physical-output/profile matrix
85: whose rows are indexed by $S_Q$, and let $M$ be the source profile Gram matrix.
86: For a prefix of $k$ profiles write $V_{Q,k}$ and $M_k$ for the corresponding
87: submatrices.  The native profile budget is
88: \[
89:  B_{Q,k,\tau}(b)=\min_c c^{\mathsf T}M_kc
````

## src-d2b99eef7a4d95e6

`papers/tpc-309-profile-prefix-shift-sensitivity/PROOF_PACKAGE.md`，原始第 34 行。

````text
32: ## Proposition 2: nested prefix feasibility
33: 
34: For a fixed ladder and target, the least-squares residual over the first `k`
35: columns is nonincreasing in `k`.  Hence, if `k(t,a)` exists, every longer
36: prefix up to the row rank remains feasible, and the maximum of the two first
37: feasible prefixes is feasible for both directional targets.
38: 
39: ### Proof
````

## src-dd4f42aa0ff6073d

`papers/tpc-308-adversarial-exclusive-completion-envelope/paper/main.tex`，原始第 103 行。

````text
101: \]
102: 
103: \begin{proposition}[Finite envelope algebra]
104: For fixed $y$ and binary $h$, the flip-subset enumeration gives the exact
105: minimum and maximum in (1).  Further,
106: \[
107:  L_{r+1}^-(y,h)\le L_r^-(y,h)\le L_r^+(y,h)
108:  \le L_{r+1}^+(y,h),                                    \tag{3}
````

## src-de9c940e519cfe79

`papers/tpc-307-common-ambient-union-shell-holdout/PROOF_PACKAGE.md`，原始第 19 行。

````text
17: ```
18: 
19: ## Assumptions and notation
20: 
21: Fix finite sets `S_L,S_R`, binary label maps `a_L,a_R`, a real matrix `V_U`,
22: and a positive semidefinite source Gram matrix `M_k`.  Let `O,E_L,E_R,U` and
23: `sigma` be as in the derivation package.  A directional target is nonzero on
24: the overlap and has a nonempty exclusive holdout.  All three normalizers are
````

## src-e3ef8a147485e961

`papers/tpc-309-profile-prefix-shift-sensitivity/paper/main.tex`，原始第 69 行。

````text
67: the parent construction; this inherited leakage is explicit below.
68: 
69: Let
70: \[
71:  P=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67).
72: \]
73: The three ordered profile ladders are the contiguous windows
74: \[
````

## src-ebd7f0c16bd8b0e9

`papers/tpc-306-two-way-operator-target-interaction/paper/main.tex`，原始第 78 行。

````text
76: operator rows; $i$ measures how much that effect changes between rows.
77: 
78: \begin{proposition}[Two-way squared-contrast identity]
79: For positive cells in (1),
80: \[
81:  d_L=m+i,\qquad d_R=m-i,\qquad m^2-i^2=d_Ld_R.                   \tag{4}
82: \]
83: If both row effects are nonzero, equal signs are equivalent to $|m|>|i|$,
````

## src-fef2014fe840107b

`papers/tpc-308-adversarial-exclusive-completion-envelope/paper/main.tex`，原始第 130 行。

````text
128: \end{proof}
129: 
130: For positive losses, TPC-308 records the conservative right-over-left
131: interval
132: \[
133:  R_r\in\left[
134:  \frac{L_r^-(y_R,h_R)}{L_r^+(y_L,h_L)},
135:  \frac{L_r^+(y_R,h_R)}{L_r^-(y_L,h_L)}\right].                  \tag{4}
````
