"""Stand-alone check of the A389839 witnesses (Python standard library only).

Reads a389839_witnesses.json. For each n (= k in our files):
  1. every stored witness N for an even t satisfies
       gcd(N, P) = gcd(N + t, P) = 1 and gcd(N + j, P) > 1 for 0 < j < t,
     where P = prime(n)#, so t is a difference of consecutive totatives;
  2. every even t below the claimed a(n) has a witness;
  3. a(n) is either a recorded non-gap (HiGHS found the covering program
     infeasible, and CP-SAT either agreed or hit its time limit) or J(n) + 2
     with J(n) = A048670(n), which is not a gap because J(n) is the largest gap.
Prints the b-file lines "n a(n)" if everything passes, and lists on stderr the
terms whose non-gap rests on HiGHS alone.
"""
import json
import math
import sys

A048670 = [2, 4, 6, 10, 14, 22, 26, 34, 40, 46, 58, 66, 74, 90, 100, 106, 118, 132, 152, 174,
           190, 200, 216, 234, 258, 264]


def primes(k):
    out, q = [], 2
    while len(out) < k:
        if all(q % p for p in out if p * p <= q):
            out.append(q)
        q += 1
    return out


def main(path="a389839_witnesses.json"):
    data = json.load(open(path))
    lines, single = [], []
    for key in sorted(data, key=int):
        r = data[key]
        k = int(key)
        P = math.prod(primes(k))
        J = A048670[k - 1]
        assert r["J"] == J, (k, "J mismatch")
        for t, N in r["witness_n"].items():
            t, N = int(t), int(N)
            assert math.gcd(N, P) == 1 and math.gcd(N + t, P) == 1, (k, t)
            assert all(math.gcd(N + j, P) > 1 for j in range(1, t)), (k, t)
        a = r["a"]
        for t in range(2, a, 2):
            assert str(t) in r["witness_n"], (k, t, "no witness")
        if a <= J:
            chk = r["nongap_checks"][str(a)]
            assert chk["highs"] == "infeasible", (k, a)
            assert chk["cpsat"] in ("infeasible", "timeout"), (k, a)
            if chk["cpsat"] != "infeasible":
                single.append(k)
        else:
            assert a == J + 2, (k, a)
        lines.append(f"{k} {a}")
    print("\n".join(lines))
    print(f"# all {len(lines)} terms verified", file=sys.stderr)
    if single:
        print(f"# non-gap confirmed by HiGHS only (CP-SAT timed out): n = {single}", file=sys.stderr)


if __name__ == "__main__":
    main(*sys.argv[1:])
