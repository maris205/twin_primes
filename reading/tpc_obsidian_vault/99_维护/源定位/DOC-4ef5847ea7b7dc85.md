---
type: "source-locator"
generated: true
---


# DOC-4ef5847ea7b7dc85 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-0c1c78e03748ef00

`papers/tpc-354-higher-origin-masked-l2-holdout/paper/main.tex`，原始第 70 行。

````text
68: with the inherited finite Euler-tail enclosure and logarithm midpoint rule.
69: 
70: \paragraph{Proposition 1 (operator polarization).}
71: For any real finite matrix $A$ and finite vectors $L,b$, putting $\beta=L-b$
72: gives
73: \begin{equation}
74:  \|A\beta\|_2^2=\|AL\|_2^2+\|Ab\|_2^2-2\langle AL,Ab\rangle.
75:  \label{eq:polar}
````

## src-276d1102e413127b

`papers/tpc-352-reciprocal-shell-adversarial-holdout/paper/main.tex`，原始第 62 行。

````text
60: those responses?
61: 
62: \section{Exact reciprocal-shell witness}
63: 
64: For the ordered shell $p_0<\cdots<p_{r-1}$ define
65: \begin{equation}
66:  \gamma_j=\frac1{p_j}-\frac1r\sum_{k=0}^{r-1}\frac1{p_k},
67:  \qquad c_I(t)=\sum_{j=0}^{r-1}\gamma_j\ind{p_j\mid t}.
````

## src-4763804eaf4d861f

`papers/tpc-353-source-native-masked-l2-polarization/paper/main.tex`，原始第 71 行。

````text
69: with the inherited finite Euler-tail enclosure and logarithm midpoint rule.
70: 
71: \paragraph{Proposition 1 (operator polarization).}
72: For any real finite matrix $A$ and finite vectors $L,b$, putting $\beta=L-b$
73: gives
74: \begin{equation}
75:  \|A\beta\|_2^2=\|AL\|_2^2+\|Ab\|_2^2-2\langle AL,Ab\rangle.
76:  \label{eq:polar}
````

## src-56a253d0604833ec

`papers/tpc-352-reciprocal-shell-adversarial-holdout/code/tpc352_reciprocal_shell_adversarial_holdout.py`，原始第 145 行。

````text
143: 
144: 
145: def matrices(origin: int, count: int, q0: int, exponent: int,
146:              law: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[int]]:
147:     values = np.arange(origin, origin + count, dtype=np.int64)
148:     differences = values[:, None] - values[None, :]
149:     distance = differences.astype(np.float64)
150:     kernel = (float(HEIGHT) ** (2 * exponent) /
````

## src-736e698f699868db

`papers/tpc-352-reciprocal-shell-adversarial-holdout/code/tpc352_reciprocal_shell_adversarial_holdout.py`，原始第 184 行。

````text
182: 
183: 
184: def fraction_matrix(origin: int, count: int, q0: int, exponent: int,
185:                     law: str, masked: bool) -> list[list[Fraction]]:
186:     values = list(range(origin, origin + count))
187:     result = [[Fraction(0) for _ in values] for _ in values]
188:     primes = shell_for(q0)
189:     for prime, sign in zip(primes, source_signs(primes, law)):
````

## src-75b80f75797faf34

`papers/tpc-353-source-native-masked-l2-polarization/paper/main.tex`，原始第 66 行。

````text
64: \begin{equation}
65:  \beta=\Lambda-b,\qquad
66:  b(t)=2C_2,1_{2\nmid t}\prod_{p\mid t,\ p>2}\frac{p-1}{p-2},
67:  \label{eq:source}
68: \end{equation}
69: with the inherited finite Euler-tail enclosure and logarithm midpoint rule.
70: 
71: \paragraph{Proposition 1 (operator polarization).}
````

## src-881dfd190cbb1b4e

`papers/tpc-351-reciprocal-shell-contrast/paper/main.tex`，原始第 79 行。

````text
77: \]
78: 
79: \section{Reciprocal-shell incidence interface}
80: 
81: For the primes in $(Q,2Q]$, define
82: \begin{equation}
83:  \gamma_j=\frac1{p_j}-\frac1r\sum_{k=0}^{r-1}\frac1{p_k}.
84:  \label{eq:gamma}
````

## src-933c5ace6e333175

`papers/tpc-354-higher-origin-masked-l2-holdout/paper/main.tex`，原始第 65 行。

````text
63: \begin{equation}
64:  \beta=\Lambda-b,\qquad
65:  b(t)=2C_2,1_{2\nmid t}\prod_{p\mid t,\ p>2}\frac{p-1}{p-2},
66:  \label{eq:source}
67: \end{equation}
68: with the inherited finite Euler-tail enclosure and logarithm midpoint rule.
69: 
70: \paragraph{Proposition 1 (operator polarization).}
````

## src-9ed3f7045e49772c

`papers/tpc-352-reciprocal-shell-adversarial-holdout/paper/main.tex`，原始第 42 行。

````text
40: \section{Question and literal defect}
41: 
42: Let $I=\{o,o+1,\ldots,o+M-1\}$ and let $R_I,E_I$ denote restriction and
43: zero extension.  For a shell prime $p$, write
44: $(P_pf)(n)=p\,\ind{p\mid n}f(n)$ and let $K_s$ have entries
45: \[
46:  K_s(u,t)=\ind{u\ne t}\frac{H^{2s}}{(H^2+(u-t)^2)^s},\qquad H=66.
47: \]
````

## src-a8fbe3752e5f6166

`papers/tpc-353-source-native-masked-l2-polarization/paper/main.tex`，原始第 83 行。

````text
81: Write $E_L=\|AL\|_2^2$, $E_b=\|Ab\|_2^2$, and, when their sum is nonzero,
82: \begin{equation}
83:  \kappa_A=\frac{2\langle AL,Ab\rangle}{E_L+E_b},qquad
84:  R_A=\frac{\|A\beta\|_2^2}{E_L+E_b}.
85:  \label{eq:kappa}
86: \end{equation}
87: Then $R_A=1-\kappa_A$.  Cauchy--Schwarz gives the exact finite envelope
88: \begin{equation}
````

## src-aa9c5d29c4fa7ad3

`papers/tpc-350-fresh-growth-signed-incidence/paper/main.tex`，原始第 61 行。

````text
59: claim, a source-uniform arithmetic estimate, or a theorem about twin primes.
60: 
61: \section{The literal masked matrix}
62: 
63: Let $I=\{o,o+1,\ldots,o+M-1\}$ and let $R_I,E_I$ denote restriction and zero
64: extension.  For a shell prime $p$, put $(P_pf)(n)=\mathbf 1_{p\nmid n}f(n)$.
65: With the same height-normalized kernel as the parent releases, the physical
66: and ideal finite matrices are
````

## src-f1f754cb6a3b4e40

`papers/tpc-350-fresh-growth-signed-incidence/paper/main.tex`，原始第 110 行。

````text
108: \end{proof}
109: 
110: \begin{proposition}[prime-incidence Gram identity]
111: For every finite matrix $D_I$,
112: \begin{equation}
113:  \|D_Ib_I\|_2^2=\sum_{j,k}\beta_j\beta_k
114:  \langle D_Ih_{p_j,I},D_Ih_{p_k,I}\rangle.
115:  \label{eq:gram}
````

## src-f6258a65a0f987b3

`papers/tpc-351-reciprocal-shell-contrast/paper/main.tex`，原始第 60 行。

````text
58: arithmetic estimate, a fixed power of $x$, or a statement about twin primes.
59: 
60: \section{Literal masked defect}
61: 
62: Let $I=\{o,o+1,\ldots,o+M-1\}$ and let $R_I,E_I$ denote restriction and zero
63: extension.  For a shell prime $p$, put
64: $(P_pf)(n)=\mathbf 1_{p\nmid n}f(n)$.  The physical matrix, its unmasked ideal,
65: and their defect are
````
