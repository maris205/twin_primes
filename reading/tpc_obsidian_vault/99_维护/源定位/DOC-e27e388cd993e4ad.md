---
type: "source-locator"
generated: true
---


# DOC-e27e388cd993e4ad 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-02cbdd7148c20f8b

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 65 行。

````text
63: \section{The exact deficit criterion}
64: 
65: \begin{theorem}[minimal four-packet criterion]
66: For any four Hilbert-space vectors with $D>0$,
67: \[
68:  0\leq q\leq4,\qquad G-D=2E,\qquad \Delta=-\frac{2E}{D}.
69: \]
70: If $G>0$, then
````

## src-0c08a7c5b00c0ec7

`papers/tpc-278-cross-scale-gain-stability/paper/main.tex`，原始第 104 行。

````text
102: \end{table}
103: 
104: \begin{theorem}[finite shell/clock instability]
105: On the declared twelve-row grid, eight rows have $E<0$ and four have
106: $E>0$.  The following fixed-scale paths reverse the sign:
107: \[
108: \begin{array}{c}
109: (128,Q=5)\to(128,Q=6),\quad
````

## src-0d4ab24eec4de0a0

`papers/tpc-276-signed-gain-endpoint-budget/paper/main.tex`，原始第 104 行。

````text
102: \]
103: 
104: \begin{theorem}[signed-gain budget]
105: Suppose that for sufficiently large \(x\), with constants \(A,b,c>0\),
106: \(\gamma\geq0\), and arbitrarily small \(\epsilon>0\),
107: \[
108:  |\Cperp(x)|\leq A x^{E_0-\sigma+\epsilon},\qquad
109:  m_D(x)\geq c x^{-\eta_D-\epsilon},\qquad
````

## src-0fab92d6eba7686e

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 48 行。

````text
46: \[
47:  D=\sum_{j=0}^3\|V_j\|^2,\qquad
48:  G=\left\|\sum_{j=0}^3V_j\right\|^2,qquad
49:  E=\sum_{0\leq j<k\leq3}\operatorname{Re}\langle V_j,V_k\rangle.
50: \]
51: TPC-277 proved the universal floor $G\leq4D$ and found a favorable sign on
52: an eight-row finite source scan.  TPC-278 then varied only a declared shell
53: endpoint or clock and found four finite sign flips.  Thus the next useful
````

## src-10780abf2f2fb85d

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 187 行。

````text
185: Then
186: \[
187:  D=3+(3-\varepsilon)^2,\qquad G=\varepsilon^2,qquad
188:  r=\frac{3+(3-\varepsilon)^2}{\varepsilon^2},
189: \qquad
190:  \Delta=1-\frac{\varepsilon^2}{3+(3-\varepsilon)^2}.
191: \]
192: As $\varepsilon\downarrow0$, the gain diverges, but $\mu=1$ throughout.
````

## src-10ead5450f3fa92c

`papers/tpc-277-four-packet-gain-floor/code/tpc277_four_packet_gain_floor_certificate.py`，原始第 123 行。

````text
121: 
122: 
123: def exact_packet_energies(scale: int, height: int, q0: int, z: int,
124:                           exponent: int) -> tuple[Fraction, Fraction,
125:                                                   list[int]]:
126:     """Return exact (D,G,shell) for the four actual source packets."""
127:     indices, beta, _weights = ENGINE.source_weights(scale, z)
128:     length = len(indices)
````

## src-17e2a561d4a3965c

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 227 行。

````text
225: \bottomrule
226: \end{tabular}
227: \caption{Coordinate transfer from the exact TPC-278 rows.  The sign is the
228: sign of the certified deficit interval, and is equivalent to the parent
229: cross-term sign.}
230: \end{table}
231: 
232: The transfer has eight positive-deficit and four negative-deficit rows,
````

## src-1c1c0413f3b09a6b

`papers/tpc-276-signed-gain-endpoint-budget/paper/main.tex`，原始第 196 行。

````text
194: these fields.\end{proof}
195: 
196: \section{Why the finite gain is not power credit}
197: 
198: The conditional theorem requires a quantified lower bound
199: \(\Dpack/\Gpack\geq b x^\gamma\) for all sufficiently large \(x\).  A finite
200: list of values at \(N=64,96,128,192,256,384\) has no such quantifier: outside
201: those points the gain can be extended by an arbitrary positive function.  Thus
````

## src-22f3546b50161703

`papers/tpc-277-four-packet-gain-floor/paper/main.tex`，原始第 70 行。

````text
68: Expansion gives $G=D+2E$.
69: 
70: \begin{theorem}[universal four-packet floor]
71: If $D>0$ and $G>0$, then
72: \[
73:  G\leq \left(\sum_{j=0}^3\|V_j\|\right)^2\leq 4D,
74:  \qquad r:=\frac{D}{G}\geq\frac14.
75: \]
````

## src-26e981b11a3bd385

`papers/tpc-277-four-packet-gain-floor/paper/main.tex`，原始第 145 行。

````text
143: \midrule
144: 192 & 32 & 6  & 5  & 1.006248221 & 0.006209423\\
145: 256 & 38 & 6  & 6  & 1.058743787 & 0.055484422\\
146: 384 & 50 & 7  & 7  & 1.124746633 & 0.110910875\\
147: 512 & 64 & 8  & 7  & 1.080616361 & 0.074602203\\
148: 768 & 86 & 9  & 9  & 1.051461797 & 0.048943098\\
149: 1024 & 108 & 10 & 10 & 1.054717352 & 0.051878688\\
150: 1536 & 150 & 12 & 12 & 1.018190110 & 0.017865141\\
````

## src-2e61350eae76ebdb

`papers/tpc-278-cross-scale-gain-stability/paper/main.tex`，原始第 79 行。

````text
77: are transferred from the hash-locked TPC-277 source audit.
78: 
79: \begin{table}[h]
80: \centering
81: \scriptsize
82: \begin{tabular}{r r r r r l}
83: \toprule
84: $N$ & $H$ & $Q$ & $z$ & $D/G$ (display) & sign of $E$\\
````

## src-3621855ecdf05701

`papers/tpc-276-signed-gain-endpoint-budget/paper/main.tex`，原始第 76 行。

````text
74: \]
75: 
76: \begin{theorem}[signed-gain margin identity]
77: Whenever \(\Dpack,\Gpack,\Wperp>0\),
78: \[
79:  m^2=r\,\md^2.
80: \]
81: In particular, \(r>1\) makes the diagonal margin proxy strictly
````

## src-63f6384fafeffd95

`papers/tpc-278-cross-scale-gain-stability/paper/main.tex`，原始第 54 行。

````text
52: \section{Exact sign/gain relation}
53: 
54: \begin{proposition}[sign equivalence]
55: If $D>0$ and $G>0$, then
56: \[
57:  E<0\Longleftrightarrow \frac DG>1,
58:  \qquad E>0\Longleftrightarrow \frac DG<1.
59: \]
````

## src-6a9b2515f3f597d5

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 235 行。

````text
233: matching the parent cross-sign census.  It does not create a growing
234: quantifier: the finite values merely illustrate the exact coordinates and
235: the instability already certified by TPC-278.  In particular, the natural
236: row at $N=192$ has a small positive deficit, while the neighboring shell and
237: clock choices cross through zero.
238: 
239: \section{Route consequence and claim firewall}
240: 
````

## src-6b0dcc85559bc509

`papers/tpc-277-four-packet-gain-floor/paper/main.tex`，原始第 113 行。

````text
111: promotion.
112: 
113: \begin{proposition}[no geometric power credit]
114: The four-packet axioms alone imply no inequality
115: $r\geq b x^\gamma$ with $b>0$ and $\gamma>0$ on a growing family.
116: \end{proposition}
117: 
118: \begin{proof}
````

## src-7cdfded53dbe390f

`papers/tpc-275-signed-four-packet-reassembly/PROOF_PACKAGE.md`，原始第 5 行。

````text
3: ## Theorem 1: signed packet Gram reassembly
4: 
5: For finite vectors `V_0,...,V_3` and
6: `Gamma_(j,k)=<V_j,V_k>`,
7: 
8: ```text
9: ||sum_j V_j||^2 = trace(Gamma) + 2 sum_(j<k) Gamma_(j,k).
10: ```
````

## src-807e91f8d11430bb

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 156 行。

````text
154: Taking reciprocals gives the gain floor when $G>0$.
155: 
156: For sharpness, let
157: \[
158:  \Gamma_\mu=(1-\mu)I_4+\mu\mathbf1\mathbf1^*.
159: \]
160: Its eigenvalues are $1-\mu$ (multiplicity three) and $1+3\mu$, so it is a
161: Gram matrix for every $\mu\in[0,1]$.  Four unit vectors realizing this Gram
````

## src-830e5f57c6143dd7

`papers/tpc-279-coherence-to-gain-theorem/PROOF_PACKAGE.md`，原始第 29 行。

````text
27: ```
28: 
29: Together with `G<=4D`, this proves the stated envelope and reciprocal floor.
30: The Gram matrix `(1-mu)I+mu 11*` is positive semidefinite with eigenvalues
31: `1-mu` (three times) and `1+3mu`; its four unit-vector realization attains
32: every bound.  Thus the constants are sharp.
33: 
34: ## Theorem 3 — coherence firewall
````

## src-85eb57d89fde607a

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 199 行。

````text
197: \section{Transfer of the TPC-278 source rows}
198: 
199: The TPC-278 certificate contains outward intervals for $r=D/G$ and for the
200: independently replayed cancellation fraction.  We transform each positive
201: gain interval $[r_-,r_+]$ into the exact reciprocal interval
202: $[1/r_+,1/r_-]$ for $q$.  The resulting deficit interval is intersected
203: with the independently stored cancellation interval.  This is a certified
204: coordinate transfer; displayed decimals below are only midpoints.
````

## src-8cab7b037f067789

`papers/tpc-275-signed-four-packet-reassembly/paper/main.tex`，原始第 155 行。

````text
153:  \Fenv=\|\Aperp\|_F^2\|\beta\|_2^2.
154: \]
155: For positive \(\Wperp\), define the conservative diagonal proxy
156: \[
157:  m_D^2=\frac{|\Cperp|^2}{\Wperp\Dpack}.
158: \]
159: When \(G<\Dpack\), it is indeed conservative: \(m_D^2\leq m^2\).
160: 
````

## src-8d14aa53281a046c

`papers/tpc-275-signed-four-packet-reassembly/paper/main.tex`，原始第 95 行。

````text
93: \section{Exact signed reassembly identities}
94: 
95: \begin{theorem}[Gram expansion and polarization]
96: For real finite packets,
97: \[
98:  G=\Dpack+2\sum_{0\leq j<k\leq3}\Gamma_{jk},
99:  \qquad
100:  \Gamma_{jk}=\frac{\|V_j+V_k\|_2^2-\|V_j-V_k\|_2^2}{4}.
````

## src-93da3cd0556a873c

`papers/tpc-268-finite-cutoff-sensitivity-obstruction/code/tpc268_cutoff_sensitivity_certificate.py`，原始第 235 行。

````text
233: 
234: 
235: def source_weights(scale: int, z: int) -> tuple[list[int], list[Fraction],
236:                                                   list[Interval]]:
237:     indices = list(range(scale // 2 + 1, scale + 1))
238:     beta = [beta_value(value, scale) for value in indices]
239:     shifted = [lambda_interval(value + 2) -
240:                comparison_interval(value, z) for value in indices]
````

## src-9af9b53b0d8ee51e

`papers/tpc-277-four-packet-gain-floor/code/tpc277_four_packet_gain_floor_certificate.py`，原始第 238 行。

````text
236:         "source_replay_status": "EXACT_FRACTION_REPLAY",
237:     }
238:     parent_row = parent_rows_by_key(parent).get((scale, exponent))
239:     if parent_row is not None:
240:         parent_gain = parse_fraction(parent_row["diagonal_to_signed_ratio"])
241:         need(parent_gain == gain, "registered parent gain mismatch")
242:         record["parent_gain_match"] = True
243:         record["parent_gain_interval"] = interval_text(parent_gain)
````

## src-a2d19d6bd325a841

`papers/tpc-275-signed-four-packet-reassembly/paper/main.tex`，原始第 87 行。

````text
85: \[
86:  V_j=\Aperp\beta^{(j)},\qquad
87:  \Gamma_{jk}=\langle V_j,V_k\rangle,qquad
88:  \Dpack=\operatorname{tr}\Gamma,qquad
89:  G=\left\|\sum_{j=0}^3V_j\right\|_2^2.
90: \]
91: All these quantities are rational on the registered rows.
92: 
````

## src-ae126d5259839529

`papers/tpc-279-coherence-to-gain-theorem/paper/main.tex`，原始第 120 行。

````text
118: \section{What pairwise coherence can and cannot prove}
119: 
120: For nonzero packet norms define
121: \[
122:  \mu=\max_{j<k}
123:  \frac{|\langle V_j,V_k\rangle|}{\|V_j\|\,\|V_k\|}\in[0,1],
124: \]
125: ignoring pairs with a zero norm (their contribution is zero).  This is an
````

## src-cdb1793fb498ba41

`papers/tpc-275-signed-four-packet-reassembly/paper/main.tex`，原始第 111 行。

````text
109: \end{proof}
110: 
111: \begin{theorem}[four-point DFT ledger]
112: Define
113: \[
114:  \widehat V_k=\frac12\sum_{j=0}^3 i^{-jk}V_j,\qquad 0\leq k\leq3.
115: \]
116: Then
````

## src-e4dc0c851e0c695a

`papers/tpc-276-signed-gain-endpoint-budget/paper/main.tex`，原始第 81 行。

````text
79:  m^2=r\,\md^2.
80: \]
81: In particular, \(r>1\) makes the diagonal margin proxy strictly
82: conservative.
83: \end{theorem}
84: 
85: \begin{proof}
86: Since \(\Gpack=\Dpack/r\), direct substitution gives
````

## src-e5d918ed117dd2f5

`papers/tpc-277-four-packet-gain-floor/paper/main.tex`，原始第 90 行。

````text
88: stronger signed floor is only a constant statement.
89: 
90: \section{The cancellation coordinate}
91: 
92: Define the dimensionless cancellation fraction
93: \[
94:  \kappaC=\frac{D-G}{D}=-\frac{2E}{D}.
95: \]
````

## src-e7e2909ff1338826

`papers/tpc-275-signed-four-packet-reassembly/paper/main.tex`，原始第 79 行。

````text
77:  (192,32,6),(256,38,6),(384,50,7),
78: \]
79: with the registered growing cutoffs \(4,4,4,5,5,5\), respectively.
80: 
81: Let \(P_3\) be the orthogonal projection onto the three declared four-block
82: Haar contrasts and set \(\Aperp=(I-P_3)A\).  Split \(\beta\) into four
83: consecutive blocks \(\beta^{(0)},\ldots,\beta^{(3)}\), padding each block by
84: zeros in the full source coordinate space.  Define
````

## src-efd76c69e762ba54

`papers/tpc-278-cross-scale-gain-stability/code/tpc278_cross_scale_gain_stability_certificate.py`，原始第 90 行。

````text
88: 
89: CASES = (
90:     # scale, H, Q, z, s, role
91:     (128, 24, 4, 5, 2, "SHELL_MINUS"),
92:     (128, 24, 5, 5, 2, "SHELL_REFERENCE"),
93:     (128, 24, 6, 5, 2, "SHELL_PLUS"),
94:     (192, 32, 5, 5, 2, "SHELL_MINUS"),
95:     (192, 32, 6, 5, 2, "NATURAL_CONTROL"),
````

## src-f569e108d0d484f8

`papers/tpc-275-signed-four-packet-reassembly/paper/main.tex`，原始第 81 行。

````text
79: with the registered growing cutoffs \(4,4,4,5,5,5\), respectively.
80: 
81: Let \(P_3\) be the orthogonal projection onto the three declared four-block
82: Haar contrasts and set \(\Aperp=(I-P_3)A\).  Split \(\beta\) into four
83: consecutive blocks \(\beta^{(0)},\ldots,\beta^{(3)}\), padding each block by
84: zeros in the full source coordinate space.  Define
85: \[
86:  V_j=\Aperp\beta^{(j)},\qquad
````

## src-f91676f00fccfd7d

`papers/tpc-276-signed-gain-endpoint-budget/paper/main.tex`，原始第 150 行。

````text
148: margin identity.\end{proof}
149: 
150: \section{Finite signed-margin transfer}
151: 
152: The TPC-275 certificate is the frozen source object.  Its rows provide an exact
153: rational \(r=\Dpack/\Gpack\) and a positive rational interval for \(\md^2\).
154: Multiplying that interval by \(r\) gives the signed-margin interval in the
155: table.  Displayed decimals are for readability; the JSON certificate stores
````
