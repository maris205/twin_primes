---
type: "source-locator"
generated: true
---


# DOC-e34b54b46fb601af 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-14a7f5a9babdfad6

`papers/tpc-321-cross-shell-profile-stability/README.md`，原始第 37 行。

````text
35: scale (X) and kernel exponent (s), is the *whole ordered normalized
36: profile* stable when the prime shell changes?  For a profile
37: (p=(p_1,ldots,p_N)), (p_j=lambda_j/operatorname{tr}(G)), we record
38: 
39: * (D_{
40: m TV}(p,q)=
41: rac12sum_j|p_j-q_j|);
42: * (D_{
````

## src-1b97a9eef5c37e57

`papers/tpc-323-signed-profile-majorization/paper/main.tex`，原始第 79 行。

````text
77:  \label{eq:block}
78: \end{equation}
79: All matrices below are finite real matrices on \(\ell^2(I_X)\).  Define
80: \begin{equation}
81:  A_{\oplus}v=(B_pv)_{p\in\mathcal S_Q},\qquad
82:  \direct=\sum_{p\in\mathcal S_Q}B_p^{\mathsf T}B_p,\qquad
83:  \signed=C_e^{\mathsf T}C_e,
84:  \quad C_e=\sum_{p\in\mathcal S_Q}e_pB_p.
````

## src-1e79c15a4aee4670

`papers/tpc-321-cross-shell-profile-stability/paper/main.tex`，原始第 124 行。

````text
122: both signs beyond $\tau$.
123: 
124: \begin{proposition}[finite metric facts]
125: The three quantities in \eqref{eq:dist}--\eqref{eq:integrated} are symmetric,
126: nonnegative, and at most one.  The $\ell^1$ profile distance obeys the triangle
127: inequality.  If $p\succeq q$, then $\DL(p,q)=\max_{r<N}d_r(p,q)$.
128: \end{proposition}
129: \begin{proof}
````

## src-2d02eca52002c6d8

`papers/tpc-320-trace-normalized-spectral-concentration/paper/main.tex`，原始第 135 行。

````text
133: \end{proof}
134: 
135: \begin{proposition}[outward quotient enclosure]
136: If $0\leq F^-\leq F\leq F^+$ and
137: $0<T^-\leq T\leq T^+$, then
138: \[
139:  \frac{F^-}{T^+}\leq\frac{F}{T}\leq\frac{F^+}{T^-}.
140: \]
````

## src-33614656eeed079e

`papers/tpc-321-cross-shell-profile-stability/paper/main.tex`，原始第 100 行。

````text
98: \section{Profile distances and the majorization firewall}
99: 
100: For two same-dimensional profiles $p,q$, define the partial-sum difference
101: \[
102:  d_r(p,q)=\sum_{j=1}^r(p_j-q_j),\qquad 1\leq r<N.
103: \]
104: We use three finite diagnostics:
105: \begin{equation}
````

## src-5d462002b5b36e2c

`papers/tpc-324-source-profile-holdout/paper/main.tex`，原始第 123 行。

````text
121: parent calculation.
122: 
123: \section{Frozen holdout protocol}
124: 
125: TPC-323 used $[321,640]$, $[641,1280]$, and $[1281,2560]$.  Before running
126: the holdout computation we fixed the two source panels in Table~\ref{tab:panels}.
127: The first is the natural continuation; the second inserts gaps.  Their
128: cardinalities are respectively $320$, $640$, and $1280$, and no source
````

## src-5dbc7cee95239584

`papers/tpc-321-cross-shell-profile-stability/paper/main.tex`，原始第 110 行。

````text
108:  \label{eq:dist}
109: \end{equation}
110: \begin{equation}
111:  \DI(p,q)=\frac1{N-1}\sum_{r<N}|d_r(p,q)|.
112:  \label{eq:integrated}
113: \end{equation}
114: The first is the $\ell^1$ distance between the ordered rank-mass vectors.  The
115: second and third measure the discrepancy of their cumulative Ky Fan profiles.
````

## src-5dc3001794d9d9dc

`papers/tpc-324-source-profile-holdout/paper/main.tex`，原始第 145 行。

````text
143: \end{table}
144: 
145: For each of the $2\times3\times4\times2=48$ rows we retain forward matrix
146: accumulation, reverse $\texttt{einsum}$ accumulation, and SciPy/NumPy
147: profile paths.  Scalar intervals expand path extrema by $10^{-12}$ and the
148: majorization tolerance is $10^{-10}$.  An independently written checker
149: rebuilds the literal blocks in reverse order.  It validates metrics and
150: outward intervals rather than requiring last-bit equality of long floating
````

## src-7293977844be2be6

`papers/tpc-320-trace-normalized-spectral-concentration/paper/main.tex`，原始第 72 行。

````text
70: The matrix $A=A_{Q,s,X}$ has rows indexed by $(p,u)\in
71: \mathcal S_Q\times I_X$ and columns indexed by $t\in I_X$.  Set
72: $G=A^*A$ and write
73: \[
74:  \lambda_1(G)\geq\lambda_2(G)\geq\cdots\geq\lambda_N(G)\geq0,\qquad
75:  T(G)=\tr(G),\qquad F_k(G)=\sum_{j=1}^k\lambda_j(G).
76: \]
77: The trace-normalized spectral distribution and its cumulative mass are
````

## src-75db5a304c38c966

`papers/tpc-324-source-profile-holdout/PROOF_PACKAGE.md`，原始第 33 行。

````text
31: 
32: ### Proof
33: 
34: Each (B_p^*B_p) and (C_e^*C_e) is positive semidefinite.  The literal
35: blocks are nonzero on every declared row, so the recorded trace checks are
36: positive.  Spectral decomposition then gives nonnegative eigenvalues whose
37: sum is the trace; normalizing produces a probability vector. (square)
38: 
````

## src-832ae805f3b4cd6b

`papers/tpc-323-signed-profile-majorization/paper/main.tex`，原始第 142 行。

````text
140:  X\in\{640,1280,2560\},\qquad Q\in\{24,36,54,80\},\qquad s\in\{1,2\},
141: \]
142: giving 24 rows.  At each row the producer accumulates the blocks in forward
143: and reverse prime order.  SciPy and NumPy symmetric eigensolvers retain
144: three profiles: SciPy-forward, NumPy-forward, and NumPy-reverse.  For every
145: law we compare its signed profile with the direct profile at the same path.
146: The stored scalar intervals expand the observed extrema by \(10^{-12}\).
147: 
````

## src-8395f5a9e57c6935

`papers/tpc-323-signed-profile-majorization/paper/main.tex`，原始第 103 行。

````text
101: \end{equation}
102: 
103: \begin{proposition}[exact amplitude--shape factorisation]
104: For every finite block family with positive traces,
105: \[
106:  T(\direct)=\sum_p\|B_p\|_F^2,\qquad
107:  T(\signed)=\left\|\sum_pe_pB_p\right\|_F^2,
108: \]
````

## src-867e5b7f3f7bd5d3

`papers/tpc-324-source-profile-holdout/paper/main.tex`，原始第 97 行。

````text
95: the precise condition so that it is not confused with the numerical result.
96: 
97: \begin{proposition}[conditional translation covariance]
98: Let $d$ be divisible by every prime in $\PP_Q$, and let
99: $T_d:\ell^2(I)\to\ell^2(I+d)$ relabel coordinates by
100: $(T_df)(u+d)=f(u)$.  Then
101: \[
102:  B_{p,I+d}^{(s)}=T_dB_{p,I}^{(s)}T_d^{-1},\quad
````

## src-951a1a55a35f058c

`papers/tpc-321-cross-shell-profile-stability/paper/main.tex`，原始第 152 行。

````text
150: transitions $24\to36$, $36\to54$, and $54\to80$, for 18 comparisons total.
151: 
152: For every row the producer accumulates the literal blocks in both forward and
153: reverse prime order.  NumPy and SciPy full symmetric eigensolvers provide
154: three retained profiles: NumPy-forward, NumPy-reverse, and SciPy-forward.
155: For each shell transition we evaluate all nine cross-path pairs.  If their
156: scalar values are $v_i$, the stored interval is
157: \[
````

## src-9ef0127495a4c5d7

`papers/tpc-321-cross-shell-profile-stability/experiments/tpc321_independent_checker.py`，原始第 119 行。

````text
117: 
118: 
119: def metrics(left: np.ndarray, right: np.ndarray) -> dict[str, Any]:
120:     delta = np.cumsum(left - right, dtype=np.float64)[:-1]
121:     tv = 0.5 * float(np.sum(np.abs(left - right), dtype=np.float64))
122:     ks = float(np.max(np.abs(delta)))
123:     integrated = float(np.mean(np.abs(delta)))
124:     minimum = float(np.min(delta))
````

## src-a6e2f058317b5c70

`papers/tpc-322-signed-projector-reassembly/paper/main.tex`，原始第 119 行。

````text
117: \end{proof}
118: 
119: Define the unnormalised reassembly ratio and the projected fraction by
120: \begin{equation}
121:  \rho_e=\frac{\|C_e\|_F^2}{D},
122:  \qquad \phi_e=\frac{\|P_eA_\oplus\|_{\HS}^2}{D}=\frac{\rho_e}{m}.
123:  \label{eq:ratios}
124: \end{equation}
````

## src-aa409cc02de6cc5a

`papers/tpc-320-trace-normalized-spectral-concentration/paper/main.tex`，原始第 97 行。

````text
95: \section{Exact algebraic firewall}
96: 
97: \begin{proposition}[finite spectral bounds]
98: For a finite PSD Gram matrix with $T(G)>0$,
99: \[
100:  0\leq C_k(G)\leq1,\qquad r_{\rm st}(G)\geq1,\qquad
101:  r_{\rm part}(G)\geq1.
102: \]
````

## src-b7c750f23e2f3886

`papers/tpc-322-signed-projector-reassembly/paper/main.tex`，原始第 160 行。

````text
158: has 16,384 vectors.
159: 
160: The producer computes the block Gram by explicit elementwise Frobenius sums
161: in forward and reverse shell order.  Each ratio is enclosed by an outward
162: guard of $10^{-12}$.  The independent checker rebuilds the blocks in reverse
163: order and uses `einsum` for each block inner product; it does not import the
164: producer.  A small $16\times16$ rational anchor with shell $\{5,7\}$ checks
165: the exact quadratic identity independently of the large floating-point
````

## src-bcd28357e6960697

`papers/tpc-321-cross-shell-profile-stability/code/tpc321_cross_shell_profile.py`，原始第 204 行。

````text
202: 
203: 
204: def profile_metrics(left: np.ndarray, right: np.ndarray) -> dict[str, Any]:
205:     need(len(left) == len(right) and len(left) > 1,
206:          "profile dimensions")
207:     delta = np.cumsum(left - right, dtype=np.float64)
208:     interior = delta[:-1]
209:     tv = 0.5 * float(np.sum(np.abs(left - right), dtype=np.float64))
````

## src-d513c88df95f6e37

`papers/tpc-323-signed-profile-majorization/PROOF_PACKAGE.md`，原始第 26 行。

````text
24: \]
25: 
26: are well-defined separately.  The matrix `G_e` is recovered spectrally from
27: the pair `(rho_e, pi_e)` together with its eigenbasis, and `pi(cG)=pi(G)` for
28: every `c>0`.
29: 
30: **Proof.** The first assertion is the trace decomposition.  The spectral
31: theorem gives `G_e=V diag(lambda(G_e)) V^T`; divide the eigenvalues by their
````

## src-db279c73d771ccf2

`papers/tpc-322-signed-projector-reassembly/paper/main.tex`，原始第 89 行。

````text
87: \section{Signed diagonal projection}
88: 
89: For $e=(e_p)_p\in\{-1,+1\}^m$, define
90: \begin{equation}
91:  E_ev=m^{-1/2}(e_pv)_p,
92:  \qquad P_e=E_eE_e^{\mathsf T}.
93:  \label{eq:projector}
94: \end{equation}
````

## src-eb5fffb1313c7308

`papers/tpc-322-signed-projector-reassembly/PROOF_PACKAGE.md`，原始第 32 行。

````text
30: ## Proposition 3 — cross-block Gram and contraction
31: 
32: Let (H_{pq}=\langle B_p,B_q\rangle_F).  Then (H\succeq0),
33: (D=\operatorname{tr}H>0), and
34: \[
35:  \rho_e=e^THe/D,\qquad 0\leq\phi_e=\rho_e/m\leq1.
36: \]
37: 
````
