---
type: "source-locator"
generated: true
---


# DOC-ee78b705591d7dfc 原始源码定位

以下是精确源路径与原始行号的邻近摘录，不是另写的证明；完整源码和 PDF 另行保留。

## src-1cfe4d1bc506b3b2

`papers/tpc-342-independent-fresh-holdout-reproduction/paper/main.tex`，原始第 50 行。

````text
48: used in TPC-338--TPC-340.
49: 
50: To obtain a genuinely independent finite check, lock the protocol to TPC-341
51: and use the three new origin/scale pairs
52: \[
53:  (40097,1024),\qquad(40609,1024),\qquad(41121,1024).
54: \]
55: Their source intervals are respectively
````

## src-648e27a98081dcca

`papers/tpc-343-cross-panel-meta-certificate/paper/main.tex`，原始第 82 行。

````text
80: nuisance columns by $\norm{y_r}$.
81: 
82: \section{Finite identities}
83: 
84: Let $N$ be any finite real matrix and let $P_N$ be the Euclidean orthogonal
85: projector onto its column space.
86: 
87: \begin{proposition}[stacked Pythagorean identity]
````

## src-7e491396f85a3ef1

`papers/tpc-340-schur-frobenius-hybrid-envelope/paper/main.tex`，原始第 53 行。

````text
51: on
52: \[
53:  I_{o,N}=\{o,\ldots,o+N/2-1\},qquad
54:  o\in\{42001,44001\},\quad N\in\{2048,4096,8192\}.
55: \]
56: The nine controls are the identity, reversal, and the seven affine maps
57: declared in TPC-338.  A control only permutes source coordinates; the matrix
58: and source construction are otherwise unchanged.
````

## src-8cded3e44b2fd2fe

`papers/tpc-344-panel-contrast-nuisance-basis/README.md`，原始第 32 行。

````text
30: 
31: ## Frozen protocol
32: 
33: ```text
34: TPC341 rows = [48097,48608], [48609,49120], [49217,49728]
35: TPC342 rows = [40097,40608], [40609,41120], [41121,41632]
36: scale       = 1024
37: operator    = all-plus, Q=54, exponent=1, H=66
````

## src-95911f352026dcba

`papers/tpc-342-independent-fresh-holdout-reproduction/README.md`，原始第 21 行。

````text
19: TPC-341 producer and certificate are hash-locked as the protocol reference;
20: TPC-342 changes only the source panel to three new, contiguous, cutoff-safe
21: windows below the earlier panel endpoint 40096.  Its reverse-shell checker
22: recomputes the projection and holdout loop without importing the TPC-342
23: producer.
24: 
25: ## Frozen design
26: 
````

## src-a1c627257342cd09

`papers/tpc-340-schur-frobenius-hybrid-envelope/paper/main.tex`，原始第 60 行。

````text
58: and source construction are otherwise unchanged.
59: 
60: \section{Two sign-free bounds}
61: 
62: Let $S=\operatorname{supp}(x)$ and let $A_S$ be the column submatrix.  The
63: support-restricted bound used by TPC-339 is
64: \begin{equation}
65:  \|Ax\|_2^2=\|A_Sx_S\|_2^2
````

## src-af9ed8b26245db67

`papers/tpc-342-independent-fresh-holdout-reproduction/paper/main.tex`，原始第 63 行。

````text
61: than padded or silently omitted.
62: 
63: \section{Projection and holdout statistic}
64: 
65: For class $C$ and control $j$, write
66: \[
67:  y_{C,j}=A P_j\beta_C.
68: \]
````

## src-c41392760ca63d70

`papers/tpc-341-fresh-holdout-nuisance-orthogonalization/paper/main.tex`，原始第 62 行。

````text
60: this rank variation instead of padding it away.
61: 
62: \section{Projection and holdout statistic}
63: 
64: For class $C$ and control $j$, write
65: \[
66:  y_{C,j}=A P_j\beta_C.
67: \]
````

## src-fd19fbed420c66c5

`papers/tpc-344-panel-contrast-nuisance-basis/paper/main.tex`，原始第 90 行。

````text
88: $>0.40$.
89: 
90: \section{Exact finite structure}
91: 
92: \begin{proposition}[contrast reparameterization]
93: \label{prop:contrast}
94: For every nuisance category $j$, let
95: \[
````

## src-fe7d1927cc952388

`papers/tpc-344-panel-contrast-nuisance-basis/paper/main.tex`，原始第 136 行。

````text
134: $Y=(1,1,1,1)^T$ has energy $2$ and residual energy $2$.
135: 
136: \section{Audited finite readout}
137: 
138: The producer creates $2\cdot3\cdot9\cdot4=216$ raw records, of which $171$
139: are nonempty.  There are six in-sample row means, 18 contrast holdouts
140: (nine omitted controls under each weighting), and four directional cross-fits.
141: Table~\ref{tab:main} gives the pooled readout.
````
