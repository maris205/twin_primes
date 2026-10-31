Proposed edit of OEIS A389839, to be submitted by the author through an OEIS account. Nothing has been submitted.

Current state (checked 2026-10-31): OFFSET 2,1. DATA has a(2)..a(12). KEYWORD nonn,more.

---

**DATA** (extended to a(26)):

```
6, 8, 12, 16, 20, 28, 32, 42, 48, 60, 68, 76, 86, 98, 108, 120, 134, 146, 166, 182, 194, 218, 230, 254, 266
```

**b-file:** replace b389839.txt with `b389839.txt` from this directory (n = 2..26).

**COMMENTS** (to add):

```
For n <= 26, every even number not occurring as a difference of consecutive totatives of prime(n)# and smaller than A048670(n) lies in [A048670(n)-8, A048670(n)-2]. - Liang Wang, Oct 31 2026

a(n) >> prime(n)*log(prime(n))*log(log(log(prime(n))))/log(log(prime(n))), the same order as the best known lower bound for A048670(n) (Ford, Green, Konyagin, Maynard, Tao); see the Wang link. - Liang Wang, Oct 31 2026
```

**LINKS** (to add):

```
Liang Wang, Gaps between totatives of primorials: the smallest missing even gap, GitHub, 2026.
  URL: https://github.com/maris205/twin_primes/blob/main/research/prize-problems/submission/note854.md
```

**EXTENSIONS** (to add):

```
a(13)-a(26) from Liang Wang, Oct 31 2026
```

**Notes for the editor** (paste into the discussion box):

```
Method: for each n and each even t <= A048670(n), the covering problem "t is a gap" was
decided by a 0-1 integer program. Every gap comes with an explicit witness N
(gcd(N, prime(n)#) = gcd(N+t, prime(n)#) = 1 and gcd(N+j, prime(n)#) > 1 for 0<j<t);
every non-gap was found infeasible by HiGHS, and for n <= 21 also by OR-Tools CP-SAT
(for n = 22, 24, 25 CP-SAT hit a one-hour limit, so a(22), a(24), a(25) rest on HiGHS alone).
If no even t <= A048670(n) is missing, a(n) = A048670(n) + 2. The witnesses and a
standard-library Python checker are in the repository linked above. Terms a(2)..a(12)
agree with the existing data. Computations were done with AI assistance (Claude, Anthropic).
```
