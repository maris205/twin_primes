# Novelty check for the new paper (2026-10-27)

Scope: Theorem 4.1, Theorem A, Theorem B, Theorem C, and also Prop 5.2. Method:
- web search, standard and extended;
- Tao's blog notes, read in segments;
- the scanned Friedlander–Iwaniec 1978 original, pp. 719–725, read page by page.

**Not checked:** the full text of Bombieri 1976 (Rend. Accad. XL), Opera de Cribro Ch. 16, Ford 2005 (Trans. AMS; returned 403), Murty–Vatwani 2017 (returned 403), and Smith 2025 (arXiv access was blocked).

## Conclusions

| Result | Verdict | Evidence | How to present it in the paper |
|---|---|---|---|
| **Thm 4.1** (one-sided parity structure for general a) | **Known (Bombieri 1976)** | FI78 p. 723, Remark I.4: "Bombieri [2] uses Theorem 1 to prove results on Σ aₙ g(n) for a wide class of functions g(n) with support on near primes". FI78 p. 721 says linear combinations of the Λ₍ₖ₎ approximate functions supported on integers with few prime factors. FI78 Lemma 1 (i), (iv) are exactly the identities our proof uses. Tao's notes (7)–(8) are the special case Λ(n+2). | Restate as Bombieri's theorem. Keep our proof as a "self-contained proof, included for completeness", note that the original was not checked line by line, and state that condition (U) is our technical form. |
| **Thm A** (log compiler, GEH + PND_log ⟹ TPC) | **Mostly known in idea; the form is new but slight** | Tao's notes: on GEH, HL ⟺ Σ μ1_R(n)μ1_R(n+2) = o(x/log²x); he calls this "a sort of Chowla conjecture restricted to almost primes" and notes the weight 1_R destroys multiplicativity at small primes. "δ bounded below ⟹ TPC" is Bombieri's. | What is new is technical: the exact identity with Λ₂♭ (no μ1_R ambiguity), the explicit one-sided terms (correcting the naive "one-point terms are o"), the log-averaged version, and PND_log as the weakest form. Present it as an explicit, testable form of Bombieri–Tao, not as a new route. |
| **Thm B** (two-sided coherence) | **Folklore level; no explicit statement found** | Tao's GEH formulations (p₁p₂ − p₃p₄ = 2, μ1_Rμ1_R) implicitly use parity structure on both sides. I found no explicit statement that u(s,r') = (δ−1)(−1)^{s+r'}. | Make it a Corollary: an explicit consequence of Bombieri's theorem applied on both sides. Its value is that it rules out "second parity parameter" worlds. |
| **Thm C** (method limitation for dilation–spectral certificates) | **No prior statement found; the most novel part** | The literature has only the heuristic: Tao's notes say Chowla progress "relies heavily on the multiplicativity of μ at small primes" and is "not yet a viable route" under 1_R; Radziwiłł's survey says there is no alternative to entropy decrement. I found no formal limitation theorem for HR/Pilatte-type expansion certificates. | Keep as a main theorem. Expect referees to question whether the certificate class (Def 6.1) faithfully captures HR/Pilatte, so §6 must compare it with their actual estimates line by line. |
| **Prop 5.2** (derived coupling law) | Known ingredients (CRT + Mertens paradox); the identification with [Wan26] is new | see paper_IIIA/NOVELTY_CHECK.md | Unchanged. |

## Related work to cite

- Murty–Vatwani, *Twin primes and the parity problem*, J. Number Theory 180 (2017) 643–659: Möbius equidistribution over shifted primes in APs, together with EH, gives prime pairs. This is the one-sided (μ(p+2)) analogue of our D₁ term and should be cited in §3.
- Pintz, arXiv:1004.1065: λ(p+2) = −1 infinitely often; also a one-sided parity result.
- Teräväinen, *On binary correlations of multiplicative functions*, Forum Math. Sigma 2018: in logarithmic density, the numbers of large prime factors of n and n+1 are independent. This is the closest unconditional result in the direction of LRC₂/RB and must be cited near Conjecture RB.
- Ford, *On Bombieri's asymptotic sieve*, Trans. AMS 357 (2005): a modern treatment of Bombieri's theorem; read it once access is available.
- Smith, arXiv:2511.14810 (2025), "GEH-2 implies TPC": a level-of-distribution hypothesis for von Mangoldt correlations. It is a different kind of hypothesis, but it is in the same "conditional route" genre and is worth citing.

## Effect on the paper's claims

The paper's real new contributions, in order:
1. Thm C (method limitation);
2. the exact compiler identity and the correction to the one-sided terms (§3);
3. the derived coupling law (Prop 5.2);
4. the explicit two-sided corollary (Thm B);
5. the numerics.

The "conditional route" GEH + PND_log ⟹ TPC is a precise restatement of Bombieri's parity criterion. It is not a weaker problem. **In particular, ρ(X) is an exact rewriting of the twin count (Thm A is an identity), so numerical evidence for ρ → 0 is numerical evidence for the twin-prime HL asymptotic itself, not independent support.**
