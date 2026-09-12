---
type: "source-locator"
generated: true
---


# DOC-eeaa751c9db6b1e3 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-011be5663d21319e

`papers/tpc-261-strict-endpoint-budget-compiler/paper/main.tex`，原始第 200 行。

````text
198: and it does not estimate the orthogonal residual left by TPC-259.
199: 
200: \section{A scaled four-packet obstruction}
201: 
202: We now show that the endpoint firewall is not merely a bookkeeping convention.
203: Let $z,w\in\HH$ be orthonormal, with $z$ the source-frozen null direction and
204: $w$ an orthogonal residual direction.  In the four-block Haar space, $w$ may
205: be the normalized scaling mode.  Set
````

## src-0a4687a092b2c7c7

`papers/tpc-254-source-backed-rank-midpoint-hybrid-mean-closure/paper/main.tex`，原始第 157 行。

````text
155: \section{Quantifier and scale firewalls}
156: 
157: The isolated corollary uses the order
158: \begin{equation}
159:  \boxed{K\text{ fixed}}\ \longrightarrow\ \gamma_0=\tfrac14
160:  \longrightarrow M\longrightarrow B_{\mathrm{H2}}
161:  \longrightarrow \delta<1-\gamma_0
162:  \longrightarrow x\geq x_0(M,K).                     \label{eq:quantifiers}
````

## src-0e22796be992bbfc

`papers/tpc-262-literal-mode-zero-cross-gram/paper/main.tex`，原始第 93 行。

````text
91: 
92: \subsection{The signed remainder operator}
93: Let \(I\) be a finite interval and \(v\in\mathbb R\).  For a coefficient
94: vector \(a\in\mathbb C^I\), define the physical residue synthesis
95: \begin{equation}
96: (S_{q,v}a)_r=\sum_{\substack{n\in I\\n\equiv r\pmod q}}
97: a_n e(vn/H),\qquad r\in\mathbb F_q^\times.
98: \label{eq:synthesis}
````

## src-17835040d9a3d0d9

`papers/tpc-263-rank-three-physical-cross-gram/paper/main.tex`，原始第 89 行。

````text
87: \end{proof}
88: 
89: \section{Three hybrid moments}
90: Write \(W_j=\sum_{u\in B_j}w(u)\).  The maximal Type-I source theorem used in
91: TPC-254 is a nonnegative sum over active intervals.  Its \(m=1\) row therefore
92: controls each of these four consecutive sums, for every fixed \(M,K\):
93: \[
94:  |W_j|\ll_{M,K}\frac{x}{(\log x)^M}.
````

## src-21adbab7b0be03ed

`papers/tpc-260-four-packet-residual-reassembly/paper/main.tex`，原始第 216 行。

````text
214: \begin{proof}
215: The matrix $(2^{-1}\ii^{-jk})_{k,j}$ is unitary, which gives
216: \eqref{eq:parseval}.  Fourier inversion at index zero gives \eqref{eq:inverse},
217: and taking norms gives \eqref{eq:modezero}.
218: \end{proof}
219: 
220: The distinction is exact in the two families
221: \begin{align*}
````

## src-288a5fc7bf480c98

`papers/tpc-260-four-packet-residual-reassembly/PROOF_PACKAGE.md`，原始第 31 行。

````text
29: shorter vectors gives the lower bound `d_max-(D-d_max)=2d_max-D`; otherwise
30: the four vectors can be joined head-to-tail to close a polygon, giving lower
31: endpoint zero.  Rotating one side continuously while keeping the other
32: three fixed fills every intermediate length.  A final common phase rotates
33: the resulting sum to any argument.  Conversely, the same triangle inequality
34: and long-side inequality apply to every choice of phases.  This proves (1).
35: 
36: Because every `V_j` is a multiple of `w` and `z` is orthogonal to `w`, the
````

## src-2a72adcea616fc59

`papers/tpc-257-four-block-haar-transverse-norm-floor/paper/main.tex`，原始第 213 行。

````text
211: \section{Adjoint normal form for bounded variation}
212: 
213: Let \(\Qx=\{q\text{ prime}:Q<q\leq2Q\}\), and let
214: \(K_H(h)=\widehat{\psi_+}(h/H)\), with the fixed smooth compactly supported
215: profile normalized by \(\int\psi_+=1\).  The literal operator is
216: \begin{equation}
217:  \Ax(u,t)=\one_{u\ne t}\sum_{q\in\Qx}q\one_{q\nmid u}\one_{q\nmid t}
218:  K_H(u-t)\left(\one_{u\equiv t\ (q)}-\frac1{q-1}\right). \label{eq:operator}
````

## src-31c2fc2963bcbb05

`papers/tpc-264-orthogonal-residual-schur-firewall/paper/main.tex`，原始第 54 行。

````text
52: \]
53: The current Route-B object is a common-clock coupling
54: \(ip{w}{g_x}\), where $g_x=A_x\beta$.  TPC-263 constructs an exact
55: rank-three source frame and proves a source-backed bound for
56: \[
57:  C_3(x)=\ip{P_3w}{P_3g_x}
58:        =O_{M,K}\!\left(\frac{x^{5/3}}{(\log x)^{M+3}}\right).
59: \]
````

## src-33261f15a9328c3f

`papers/tpc-260-four-packet-residual-reassembly/paper/main.tex`，原始第 166 行。

````text
164: side is longer than the other three combined, reversing the shorter sides gives
165: the lower endpoint $d_{\max}-(D-d_{\max})$.  Otherwise the four sides close to a
166: polygon, so the lower endpoint is zero.  Rotating one side continuously fills the
167: interval between the two endpoints; a common rotation supplies any argument.
168: Since $z\perp w$, every member of the family has $\ip{z}{G}=0$.  The same two
169: triangle inequalities apply to every choice of phases, proving sharpness.
170: \end{proof}
171: 
````

## src-4480b47a659a6749

`papers/tpc-262-literal-mode-zero-cross-gram/paper/main.tex`，原始第 162 行。

````text
160: \end{proof}
161: 
162: \subsection{The phase-character firewall}
163: The packet index has its own Fourier characters.  For two vectors \(X,Y\)
164: write
165: \begin{equation}
166: E_j=\norm{X+\ii^jY}^2,\qquad
167: F_k=\frac14\sum_{j=0}^3\ii^{kj}E_j.
````

## src-46cf404457c04675

`papers/tpc-262-literal-mode-zero-cross-gram/paper/main.tex`，原始第 54 行。

````text
52: \end{enumerate}
53: \section{The literal reduced-residue fiber}
54: For an odd prime \(q\), write \(m_q=q-1\) and let
55: \({\bf 1}_q\in{\mathbb R}^{m_q}\) be the all-ones vector.  Define
56: \begin{equation}
57: C_q=I_{m_q}-\frac{1}{m_q}{\bf 1}_q{\bf 1}_q^{\mathsf T}.
58: \label{eq:C}
59: \end{equation}
````

## src-582cfd88ec7510f5

`papers/tpc-260-four-packet-residual-reassembly/paper/main.tex`，原始第 296 行。

````text
294: \end{center}
295: 
296: This is a scoped Route-B advance: it removes a tempting but invalid promotion rule
297: and leaves a sharply stated positive target.  The next theorem should control
298: \[
299:  \left|\ip{w_\perp}{\sum_{j=0}^3V_j}\right|
300:  \quad\text{or equivalently the mode-zero/cross-Gram quantity in
301:  \eqref{eq:modezero}--\eqref{eq:crossgram},}
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

## src-602cc5b7c8f95d7c

`papers/tpc-261-strict-endpoint-budget-compiler/paper/main.tex`，原始第 113 行。

````text
111: \section{The strict budget compiler}
112: 
113: \begin{theorem}[finite-lane endpoint compiler]
114: Let $\mathcal L$ be finite and nonempty.  Suppose that for every $j\in\mathcal L$
115: and every $\varepsilon>0$, there is a constant $C_{j,\varepsilon}$ such that,
116: for all sufficiently large $x$,
117: \begin{equation}
118:  |T_j(x)|\leq C_{j,\varepsilon}
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

## src-6c0818b11e8c000d

`papers/tpc-264-orthogonal-residual-schur-firewall/code/tpc264_schur_firewall_certificate.py`，原始第 192 行。

````text
190: 
191: 
192: def dimension_audit() -> dict[str, Any]:
193:     a = Fraction(3, 2)
194:     b = Fraction(2)
195:     radius = a * b
196:     disk_points = {
197:         "zero": (Fraction(0), Fraction(0)),
````

## src-6c715ec8410ed27d

`papers/tpc-264-orthogonal-residual-schur-firewall/paper/main.tex`，原始第 138 行。

````text
136: \end{definition}
137: 
138: \begin{theorem}[exact Schur feasible set]
139: Let $m=\dim\ker(P)$, allowing $m=\infty$.  With $a,b,c,z$ as above, the
140: possible residual values, when $p,q,a,b$ are fixed, are as follows.
141: \begin{enumerate}
142:  \item If $m\geq2$, the set is the closed disk
143:  \[
````

## src-721420cdbd37d7b3

`papers/tpc-260-four-packet-residual-reassembly/paper/main.tex`，原始第 193 行。

````text
191: term in \eqref{eq:tpc259-split} says nothing by itself about the second.
192: 
193: \section{The missing DFT mode}
194: 
195: The polygon theorem describes the size ambiguity.  The following identity locates
196: its information-theoretic source.  Define the four-point packet DFT by
197: \begin{equation}
198:  \Vhat_k=\frac12\sum_{j=0}^3\ii^{-jk}V_j,
````

## src-7495744de0242504

`papers/tpc-262-literal-mode-zero-cross-gram/paper/main.tex`，原始第 188 行。

````text
186: The theorem does not replace the smooth kernel or prove a favorable sign.
187: 
188: \begin{corollary}[endpoint translation]
189: The current V59 ledger is
190: \begin{equation}
191: E_0=\frac53=\frac{2000}{1200},\qquad
192: E_*=\frac{1997}{1200},\qquad E_0-E_*=\frac1{400}.
193: \label{eq:gap}
````

## src-7c03d8a926e0b6b2

`papers/tpc-257-four-block-haar-transverse-norm-floor/paper/main.tex`，原始第 270 行。

````text
268: \section{Main theorem and norm floors}
269: 
270: \begin{theorem}[Three-mode adjoint asymptotics]\label{thm:main}
271: For each \(i=0,1,2\),
272: \begin{equation}
273:  \boxed{\displaystyle
274:  \ip{z_i}{\Ax\beta}
275:  =-\left(\frac92\kappa_i+o(1)\right)
````

## src-8e8b17fc04d07fb0

`papers/tpc-264-orthogonal-residual-schur-firewall/paper/main.tex`，原始第 246 行。

````text
244:  \frac53-\frac{1997}{1200}=\frac1{400}.
245: \]
246: Therefore a future literal theorem needs at least one of the following:
247: \begin{enumerate}
248:  \item a residual-radius estimate
249:  \[
250:   \norm{(I-P_3)w}\,\norm{(I-P_3)g_x}
251:        \ll x^{5/3-\delta},\qquad \delta>\frac1{400},
````

## src-a160ceed54b9f73e

`papers/tpc-264-orthogonal-residual-schur-firewall/paper/main.tex`，原始第 198 行。

````text
196: \section{An exact finite audit}
197: 
198: For a concrete fixture take an ambient space with five coordinates and let $P$
199: keep the first three.  Fix
200: \[
201:  p=(1,0,0),\qquad q=(2+i,0,0),\qquad a=\frac32,\qquad b=2.
202: \]
203: Then $c=\ip{p}{q}=2+i$ and the Schur radius is $ab=3$.  In the last two
````

## src-aa55368e5a8deecd

`papers/tpc-263-rank-three-physical-cross-gram/paper/main.tex`，原始第 122 行。

````text
120: packet diagonals.
121: 
122: \begin{theorem}[rank-three physical cross-Gram channel]
123: For every fixed admissible \(K\) and every fixed \(M>0\),
124: \[
125:  |C_3(x)|\ll_{M,K}\frac{x^{5/3}}{(\log x)^{M+3}}.
126: \]
127: \end{theorem}
````

## src-c2191eef07193054

`papers/tpc-260-four-packet-residual-reassembly/paper/main.tex`，原始第 139 行。

````text
137: $G=\sum_jV_j$.
138: 
139: \begin{theorem}[polygon completion]
140: Fix nonnegative packet lengths $d_0,d_1,d_2,d_3$.  Among the families
141: \[
142:  V_j=d_j e^{\ii\theta_j}w,
143:  \qquad \theta_j\in\mathbb R,
144:  \]
````

## src-c68edea3c5d74dc0

`papers/tpc-260-four-packet-residual-reassembly/paper/main.tex`，原始第 91 行。

````text
89: \section{The four-block interface}
90: 
91: Let $B_0,B_1,B_2,B_3$ be consecutive nonempty blocks with lengths
92: $s_0,s_1,s_2,s_3$ and $N=s_0+s_1+s_2+s_3$.  On blockwise-constant vectors use
93: the weighted inner product
94: \[
95:  \ip{u}{v}_s=\sum_{j=0}^3s_j\,\overline{u_j}v_j.
96: \]
````

## src-d281a54c10631719

`papers/tpc-263-rank-three-physical-cross-gram/paper/main.tex`，原始第 55 行。

````text
53: claimed uniform in either parameter.
54: 
55: \section{The source-only rank-three frame}
56: Let \(I_x=(x/2,x]\cap\mathbb Z\), \(N=|I_x|\),
57: \(\ell=\lfloor N/2\rfloor\), and \(r=N-\ell\).  Split the two rank
58: children into consecutive blocks \(B_1,B_2,B_3,B_4\), with sizes
59: \(s_1,s_2,s_3,s_4\).  For adjacent sets of sizes \(p,q\), define
60: \[
````

## src-f319b47f09b18690

`papers/tpc-264-orthogonal-residual-schur-firewall/paper/main.tex`，原始第 226 行。

````text
224: large enough to exercise every branch of the theorem.
225: 
226: \section{Endpoint-scale consequence}
227: 
228: The rank-three channel provides a center that is small in fixed logarithmic
229: powers.  The Schur theorem says that this fact is not enough if the residual
230: radius is left at the natural baseline scale.  Consider the synthetic choice
231: \[
````

## src-f9394fa659185aa3

`papers/tpc-264-orthogonal-residual-schur-firewall/PROOF_PACKAGE.md`，原始第 83 行。

````text
81: not a literal prime-shell construction. `(square)`
82: 
83: ## Corollary — minimum missing theorem
84: 
85: On the actual V59 clock, TPC-263 supplies a logarithmically small center
86: `c=C_3`.  A sufficient next input for a fixed-power endpoint payment is either
87: 
88: ```text
````

## src-fc2f3e0794d0b292

`papers/tpc-261-strict-endpoint-budget-compiler/paper/main.tex`，原始第 151 行。

````text
149: larger than $1/400$.
150: 
151: \begin{table}[t]
152: \centering
153: \caption{Exact budget examples.  ``Local'' and ``conditional'' labels do not
154: transfer credit to the current literal whole object.}
155: \label{tab:budget}
156: \begin{tabular}{lcccc}
````
