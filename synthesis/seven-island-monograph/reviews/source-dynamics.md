TPC_AGENT_RESULT_V1

task_id: `synth-dynamics-geometry`  
mode: `READ_ONLY source audit`  
scope: Island 5, image Bridge B, and island 7 only  
baseline_HEAD: `d37c92b8a66bbd3d9084b1597d346429a9285302`  
TPC_HANDOFF_sha256: `fee6147d2a01b324b723949a19c5a4ddd470237a315974b37acd18bd09e82bc8`  
baseline_verification: matched at entry and final recheck  
files_changed: `[]`

The consolidation can present a genuine metric recurrence theorem and exact nonautonomous sieve geometry. It cannot present recurrence at the distinguished arithmetic seed, an attached Logistic carrier, or a TPC Hénon lifting theorem as proved. The current handoff explicitly leaves the distinguished-seed bridge open: [TPC_HANDOFF.md, lines 126–134](/root/autodl-tmp/math_research3/twin_primes/TPC_HANDOFF.md:126).

## Eight concrete source items

### 1. Exact arithmetic moving-target encoding

**Status: exact identity and source-backed mass estimate.**

On \((\widehat{\mathbb Z},\mu)\), with Haar probability and \(T(x)=x+1\), set
\[
Q_n=\prod_{p\le\sqrt{n+2}}p,\qquad
f_n(r)=\prod_{p\le\sqrt{n+2}}
  \mathbf1_{p\nmid r}\mathbf1_{p\nmid r+2},
\qquad E_n=\{f_n=1\}.
\]
Then, for \(n\ge3\),
\[
Z_n(0):=\mathbf1_{E_n}(T^n0)=1
\iff n,n+2\text{ are both prime}.
\]
Moreover,
\[
\alpha_n:=\mu(E_n)
=\frac12\prod_{2<p\le\sqrt{n+2}}(1-2/p)
\asymp(\log n)^{-2},
\qquad \sum_n\alpha_n=\infty.
\]

**Anchors:** [TPC_COMPASS.md, lines 5800–5822](/root/autodl-tmp/math_research3/twin_primes/TPC_COMPASS.md:5800); original metric-proof definitions in [research/tpc-big-road/README.md, lines 5803–5820](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/README.md:5803).

**Qualifier:** the base map is autonomous; the arithmetic cutoff and targets move with \(n\). Calling this a “nonautonomous route” must not suggest that the odometer itself is mixing or stage-dependent.

**Placement:** opening paragraph of the island-5 section.

### 2. Exact resonance summation and Haar moving-target variance

**Status: proved in the source, with a complete CRT/Abel argument.**

For \(m<n\), \(d=n-m\), and \(q=\sqrt{m+2}\),
\[
\operatorname{Cov}_{\mu}(Z_m,Z_n)
=\alpha_m\alpha_n\bigl(K_q(d)-1\bigr).
\]
The local factors of \(K_q=\prod_{p\le q}k_p\) are
\[
k_2(d)=2\mathbf1_{2\mid d},\qquad k_3(d)=3\mathbf1_{3\mid d},
\]
and, for \(p\ge5\),
\[
k_p(d)=1-\frac4{(p-2)^2}
+\frac{2p}{(p-2)^2}\mathbf1_{p\mid d}
+\frac p{(p-2)^2}
 \bigl(\mathbf1_{p\mid d-2}+\mathbf1_{p\mid d+2}\bigr).
\]
For every integer interval \(I\) and \(q\ge2\),
\[
\left|\sum_{d\in I}(K_q(d)-1)\right|
\le D(q):=6\prod_{5\le p\le q}(1-2/p)^{-2}
\ll\log^4(2q).
\]
Each local factor has complete-residue mean one. Expanding into CRT classes gives the interval discrepancy bound. Abel summation then uses monotonicity of \(\alpha_n\) and, for \(q\ge3\),
\[
\alpha(q)^2D(q)=\frac16.
\]
Consequently,
\[
\operatorname{Var}_{\mu}\!\left(\sum_{3\le n\le N}Z_n\right)\ll N,
\qquad
\operatorname{Var}_{\mu}\!\left(\sum_{X<n\le2X}Z_n\right)
\le X/2+O(1).
\]
Since \(A_N:=\sum_{3\le n\le N}\alpha_n\asymp N/\log^2N\), Chebyshev and Borel–Cantelli along square indices imply infinitely many hits for Haar-almost every seed.

**Anchors:** [README.md, lines 5816–5866, Theorem 4.1](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/README.md:5816); [lines 5868–5929, Theorem 4.2 and its boundary](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/README.md:5868).

**Placement:** principal positive proposition, including a short proof. This is actual metric progress, not a finite experiment.

### 3. Exact missing seed input and a conditional local criterion

**Status: pointed recurrence remains open; the following sufficient lemma has an explicit proof in the archived source.**

The missing conclusion is
\[
S_N(0):=\sum_{3\le n\le N}Z_n(0)\longrightarrow\infty,
\]
which, by item 1, is equivalent to TPC. Haar-a.e. recurrence does not establish it.

A more explicit sufficient condition isolates a local discrepancy obligation. Choose integers \(q_N\mid Q_N\), and define
\[
U_N=q_N\widehat{\mathbb Z},\qquad
V_N=\|S_N-A_N\|_2,\qquad
\Omega_N=\sup_{u\in U_N}\bigl(S_N(u)-S_N(0)\bigr).
\]
Then
\[
S_N(0)\ge A_N-\sqrt{q_N}\,V_N-\Omega_N.
\]
Thus, along an unbounded sequence \(N_j\), the condition
\[
\Omega_{N_j}+\sqrt{q_{N_j}}\,V_{N_j}
\le(1-\eta)A_{N_j},\qquad \eta>0\text{ fixed},
\]
implies \(S_{N_j}(0)\ge\eta A_{N_j}\to\infty\).

The known \(V_N\ll\sqrt N\) pays the variance loss when
\[
q_N=o(N/\log^4N).
\]
**The missing input is a sufficiently small one-sided \(\Omega_N\) on such coarse cylinders.** Taking \(q_N=Q_N\) makes \(\Omega_N=0\), but incurs the enormous \(\sqrt{Q_N}\) evaluation loss.

**Anchors:** [recon-distinguished-seed.md, lines 78–105](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/research-rounds/2026-09-09-multi-agent-recon/agent-reports/recon-distinguished-seed.md:78). Its same-odometer, exact-mass cylinder-swap counterexample appears at [lines 34–76](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/research-rounds/2026-09-09-multi-agent-recon/agent-reports/recon-distinguished-seed.md:34).

**Qualifiers:** this sufficient condition gives a natural-scale subsequential lower bound, stronger than infinitude alone. The counterexample changes the events; it disproves a metric-only inference, not recurrence for the unchanged arithmetic events. The archive does not give every scout derivation the independent-audit status of its designated proof tasks.

**Placement:** immediately after the metric proposition, as “the distinguished-seed gap.”

### 4. Exact replication–deletion geometry and orthogonal forcing

**Status: proved finite-dimensional identities, valid at every declared stage.**

Let \(P_k=\prod_{j\le k}p_j\), \(V_k=\mathbb C^{\mathbb Z/P_k\mathbb Z}\), with normalized counting inner product. For a new odd prime \(p\nmid P_k\), define
\[
(R_pf)(r+jP_k)
=f(r)\mathbf1_{p\nmid r+jP_k}\mathbf1_{p\nmid r+jP_k+2}.
\]
Exactly \(p-2\) children survive for every parent residue. Hence, with \(\alpha_p=1-2/p\),
\[
R_p^*R_p=\alpha_p I,\qquad
\|R_{b:a}f\|=\sqrt{\beta_{b:a}}\|f\|,
\quad
\beta_{b:a}=\prod_{a<j\le b}(1-2/p_j).
\]

For \(B_k\) the pair-survivor indicator, \(a_k=\operatorname{mean}(B_k)\), \(W_k=B_k-a_k\mathbf1\), and \(g_{k,p}=R_p\mathbf1-\alpha_p\mathbf1\),
\[
W_{k+1}=R_pW_k+a_kg_{k,p},
\qquad g_{k,p}\perp R_p(V_k^0),
\]
\[
\|W_k/a_k\|_2^2=a_k^{-1}-1\asymp(\log p_k)^2.
\]

**Anchors:** [bridge_b_physical_intertwiner.md, lines 21–112](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_physical_intertwiner.md:21); [lines 114–153](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_physical_intertwiner.md:114).

**Placement:** structural paragraph explaining why stage evolution is forced, rather than a homogeneous contracting model.

### 5. Scoped obstruction to a uniformly contracting full-space carrier

**Status: proved incompatibility, not a prohibition of all dynamics.**

One cannot simultaneously have
\[
c\|f\|\le\|J_kf\|\le C\|f\|,
\quad \|Q_{b:a}\|\le C_Q\theta^{b-a},\quad 0<\theta<1,
\quad J_{k+1}R_{p_{k+1}}=Q_kJ_k
\]
on the full centered spaces, uniformly in stage. These assumptions imply
\[
c\sqrt{\beta_{b:a}}\le C_QC\theta^{b-a},
\]
contradicting the sieve product’s slower decay.

For a quasi-intertwiner,
\[
\Delta_{b:a}
=\sum_{a\le j<b}Q_{b:j+1}\operatorname{Err}_jR_{j:a},
\qquad
\|\Delta_{b:a}\|
\ge c\sqrt{\beta_{b:a}}-C_QC\theta^{b-a}.
\]

**Anchor:** [bridge_b_physical_intertwiner.md, lines 155–234](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_physical_intertwiner.md:155).

**Qualifier/placement:** a short obstruction remark. Noncoercive observable quotients, nonuniform products, and estimates after physical evaluation remain outside this no-go.

### 6. Surviving deterministic-return interface

**Status: proposed theorem contract, not a constructed carrier.**

The source requires a predeclared affine-pattern class independent of future prime hits, an actual fixed-\(h_0=2\) member, and
\[
J_{k+1}R_p=Q_kJ_k+\operatorname{Err}_k,
\qquad
\ell(f)=\Lambda^{\mathrm{dyn}}_{X,A,\ell}(J_{k_X}f).
\]
The return identity must hold on the declared domain, not just a fitted trajectory. Its propagated defects must satisfy
\[
\sup_{A,\ell}\sum_{j_0\le j<k_X}
\left|
\Lambda^{\mathrm{dyn}}_{X,A,\ell}
\!\left(Q_{k_X:j+1}\operatorname{Err}_j f_{j,X,A}\right)
\right|
\le\varepsilon(X)\frac{X}{(\log X)^2},
\quad \varepsilon(X)\to0,
\]
or supply the stronger literal Type-II estimate required by the analytic reassembly.

**Anchor:** [bridge_b_physical_intertwiner.md, lines 278–358](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_physical_intertwiner.md:278).

**Qualifier:** this error budget alone is not a prime-producing estimate. The dynamical main output, exact physical return, normalization, and relevant analytic estimates remain obligations.

**Placement:** end of island 5, explicitly labeled “proposed interface to the analytic core.”

### 7. Stationary mixing cannot factor onto the arithmetic clock

**Status: proved elementary obstruction.**

If a probability-preserving mixing system admitted
\[
\pi(Ty)=\pi(y)+1\pmod M,\qquad M\ge2,
\]
then \(f(y)=e^{2\pi i\pi(y)/M}\) would be a nonconstant mean-zero eigenfunction with
\[
\int(f\circ T^n)\overline f\,d\nu=e^{2\pi in/M}.
\]
This contradicts mixing; the eigenfunction also rules out weak mixing. A factor onto the profinite odometer would induce such a finite factor.

**Anchor:** [bridge_b_euler_zero_axis_and_kernel_carrier.md, lines 758–802](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_euler_zero_axis_and_kernel_carrier.md:758).

**Qualifier/placement:** transition into island 7. The argument does not rule out stage-dependent diagrams \(\pi_{j+1}\circ F_j=R_j\circ\pi_j\).

### 8. Hénon lifting: precise requirement, no attached TPC theorem

**Status: proposed arithmetic attachment; external geometric result reported by the repository, not independently reverified here.**

The explicit proposed diagram is
\[
\rho_{k+1}\circ H_k=F_k\circ\rho_k,\qquad
E_{H,k}=\rho_k^{-1}(E_{F,k}),\qquad
(\rho_k)_*\mu_{H,k}=\mu_{F,k}.
\]
It must additionally preserve the specified seed and the physical functional. Neither area preservation nor reversibility supplies these properties.

**Anchors:** [TPC_COMPASS.md, lines 6185–6193](/root/autodl-tmp/math_research3/twin_primes/TPC_COMPASS.md:6185); [bridge_b_physical_intertwiner.md, lines 378–391](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_physical_intertwiner.md:378).

The repository describes Boroński–Štimac’s Wang–Young Hénon result as a natural-extension description over a densely branching metric tree, expressly **not** a Logistic interval, residue odometer, or TPC physical section: [bridge_b_euler_zero_axis_and_kernel_carrier.md, lines 946–969](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_euler_zero_axis_and_kernel_carrier.md:946).

**Placement:** brief optional geometric epilogue, not a theorem asserting island 7 reaches island 6.

## Recommended coherent consolidation narrative

Allocate approximately 2–3 pages after the analytic core:

1. **Arithmetic targets and metric recurrence:** items 1–2 supply the positive result and its short CRT/Abel proof.
2. **Why the distinguished seed remains missing:** item 3 separates almost-everywhere recurrence from arithmetic recurrence and exposes a concrete one-sided local discrepancy obligation.
3. **What a nonautonomous carrier must preserve:** compress items 4–6 into the exact forced recursion, its contraction obstruction, and a clearly conditional physical-return interface.
4. **Optional geometry:** items 7–8 explain why stationary mixing and geometric lifting cannot bypass the arithmetic attachment.

The organizing conclusion is: *the arithmetic event coding and metric recurrence are available, but the specified arithmetic orbit is not controlled. A useful dynamical or geometric construction must return information at that orbit, or directly control the corresponding physical functional.*

## Issues and claim boundaries

- Do not import old roadmap priority labels as current instructions. Image Bridge B is the distinguished-seed bridge, not repository analytic Gate B.
- Do not assert that the physical count equals its Haar mean asymptotically. The original TeX labels the endpoint coefficient a benchmark and makes the twin value \(e^{2\gamma}/4\) conditional on Hardy–Littlewood: [TPC-1 main.tex, lines 759–793](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-1-two-scale-prime-sieve-correlations/main.tex:759).
- Do not equate two-dimensional Hénon phase space with a two-dimensional observable carrier. The source explicitly excludes that inference: [bridge_b_observable_rank.md, lines 299–310](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_observable_rank.md:299).
- Archived reconnaissance links contain historical old-repository paths. The anchors above refer to the current standalone repository.
- No TPC-specific geometric lifting proof was located in the audited sources. The external Hénon theorem should remain a qualified literature remark unless its original theorem and hypotheses are separately checked.

No files, generators, staging, synchronization, or uploads were used or changed.
