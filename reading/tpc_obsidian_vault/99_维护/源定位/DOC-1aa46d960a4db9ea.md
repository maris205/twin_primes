---
type: "source-locator"
generated: true
---


# DOC-1aa46d960a4db9ea 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-014afce1e7d550f8

`papers/tpc-337-control-covariance-masked-response/paper/main.tex`，原始第 65 行。

````text
63: \]
64: 
65: \section{Exact covariance structure}
66: 
67: Because $\sum_jz_{C,j}=0$, finite expansion gives
68: \begin{equation}\label{eq:class}
69:  \frac15\sum_j\|y_{C,j}\|_2^2
70:  =\|\bar y_C\|_2^2+\frac15\sum_j\|z_{C,j}\|_2^2.
````

## src-0f34af54001f9f48

`papers/tpc-335-twin-isolated-source-norm/paper/main.tex`，原始第 50 行。

````text
48: word ``twin-isolated'' means a coordinate mask, not a new asymptotic source.
49: 
50: \section{Finite source and masks}
51: 
52: For $o\in\{42001,44001\}$ and
53: $N\in\{2048,4096,8192\}$, let
54: \[
55:  I_{o,N}=\{o,o+1,\ldots,o+N/2-1\}.
````

## src-2e94c0a4b9b72a99

`papers/tpc-335-twin-isolated-source-norm/paper/main.tex`，原始第 76 行。

````text
74: \]
75: 
76: \section{Exact masked norm identity}
77: 
78: The classes are disjoint and exhaustive.  Consequently,
79: \begin{equation}\label{eq:normsplit}
80:  \|\beta\|_2^2=\sum_{C\in\{\mathsf T,\mathsf B,\mathsf P,\mathsf Z\}}
81:  \|\beta_C\|_2^2.
````

## src-2eefb28433ff6309

`papers/tpc-339-mask-aware-frobenius-envelope/paper/main.tex`，原始第 61 行。

````text
59:  F(S)^2=\|A_S\|_F^2=\sum_{t\in S}\sum_u|A(u,t)|^2.
60: \]
61: For a nonzero $x$, the occupancy is
62: \[
63:  \eta(A,x)=\frac{\|Ax\|_2^2/\|x\|_2^2}{F(\operatorname{supp}x)^2}\leq1.
64: \]
65: This is deliberately independent of covariance signs and of the signs of the
66: source entries.  A small $\eta$ measures slack in the bound, not a payment of
````

## src-40801676cea2c923

`papers/tpc-338-growing-control-covariance-spectrum/paper/main.tex`，原始第 31 行。

````text
29: \end{abstract}
30: 
31: \section{Question and nested ensembles}
32: 
33: Write the parent-locked source as
34: \[
35:  \beta=\sum_{C\in\{T,B,P,Z\}}\beta_C,
36:  \qquad \beta(t)=\Lambda(t+2)-b^{(2)}(t),
````

## src-4187289828844735

`papers/tpc-336-masked-signed-gram-response/code/tpc336_masked_signed_gram_response.py`，原始第 139 行。

````text
137:     vectors = {c: beta * masks[c] for c in CATEGORIES}
138:     outputs = {c: matrix @ vectors[c] for c in CATEGORIES}
139:     source_norms = {c: float(v @ v) for c, v in vectors.items()}
140:     self_metrics = {}
141:     for c in CATEGORIES:
142:         e = float(outputs[c] @ outputs[c])
143:         d = float(np.sum(column_energy * vectors[c] * vectors[c]))
144:         if source_norms[c] == 0.0:
````

## src-747e22b9fa659b8f

`papers/tpc-336-masked-signed-gram-response/paper/main.tex`，原始第 72 行。

````text
70: \]
71: with height $H=66$ and the same residue and divisibility masks as the parent
72: model.  For each class let $y_C=C\beta_C$ and define, when the denominator
73: is nonzero,
74: \[
75:  G_C=\frac{\|y_C\|_2^2}{\|\beta_C\|_2^2}.
76: \]
77: 
````

## src-82a4bb8c3624147f

`papers/tpc-335-twin-isolated-source-norm/code/tpc335_twin_isolated_source_norm.py`，原始第 82 行。

````text
80: 
81: 
82: def classify(source: Any, t: int, lam: float, comp: float) -> str:
83:     if lam * comp == 0.0:
84:         return "zero_support"
85:     pp = source.prime_power(t + 2)
86:     need(pp is not None, "cross support prime power")
87:     if pp[1] == 1:
````

## src-966e452346d76f3f

`papers/tpc-339-mask-aware-frobenius-envelope/paper/main.tex`，原始第 77 行。

````text
75: every record.  Mutation stress changes both structural and semantic fields.
76: 
77: For an exact anchor take
78: \[
79:  A=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad x=(3,0).
80: \]
81: Then $\|Ax\|^2=45$, $\|x\|^2=9$, and $F(\{0\})^2=5$, so equality holds in
82: \eqref{eq:bound}.  The anchor proves the inequality's algebraic interface only.
````

## src-de305c7179a453bd

`papers/tpc-339-mask-aware-frobenius-envelope/paper/main.tex`，原始第 48 行。

````text
46: can go.
47: 
48: \section{Support-restricted bound}
49: 
50: If $x$ is supported on $S$, let $A_S$ denote the columns of $A$ indexed by
51: $S$.  Then
52: \begin{equation}\label{eq:bound}
53:  \|Ax\|_2^2=\|A_Sx_S\|_2^2
````

## src-f990ba793b871226

`papers/tpc-336-masked-signed-gram-response/paper/main.tex`，原始第 78 行。

````text
76: \]
77: 
78: \section{Finite output-Gram identity}
79: Since $C\beta=\sum_Cy_C$, finite bilinearity gives
80: \begin{equation}\label{eq:response}
81:  \|C\beta\|_2^2=\sum_C\|y_C\|_2^2+
82:  2\sum_{C<D}\langle y_C,y_D\rangle.
83: \end{equation}
````
