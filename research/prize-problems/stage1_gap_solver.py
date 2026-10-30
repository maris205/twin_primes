"""Exact decision of which even gaps occur among integers coprime to P_k (Erdos #854).

Lemma 1.1 (STAGE1_GAPS.md): the even number t = 2m is a gap between consecutive
integers coprime to P_k if and only if the points 1, ..., m-1 can be covered by
choosing one residue class c_p (mod p) for each odd prime p <= p_k, subject to
c_p not in {0, m mod p}.

The search is a depth-first search: take the uncovered point with the fewest
admissible primes, branch on the prime that covers it, and prune when the
remaining primes cannot cover the remaining points even in the best case.
A successful search returns a certificate (the classes), which is verified
independently by `check_certificate`.
"""
import json
import sys
import time

def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


PR = primes_upto(2000)


def gap_occurs(k, t, node_limit=None):
    """Return (True, certificate) / (False, None) / (None, None) if the node limit is hit."""
    assert t % 2 == 0 and t >= 2
    m = t // 2
    pts = m - 1
    if pts == 0:
        return True, {}
    odd = PR[1:k]
    full = (1 << pts) - 1
    # masks[p] = list of (class, bitmask of points i in [1, m-1] with i = class mod p)
    masks = {}
    for p in odd:
        lst = []
        for c in range(p):
            if c == 0 or c == m % p:
                continue
            b = 0
            i = c if c > 0 else p
            while i <= pts:
                b |= 1 << (i - 1)
                i += p
            if b:
                lst.append((c, b))
        masks[p] = lst
    # point -> admissible primes with the class that covers it
    cover_of = []
    for i in range(1, pts + 1):
        opts = [p for p in odd if i % p != 0 and i % p != m % p]
        cover_of.append(opts)
    nodes = [0]

    def bound(unc, unused):
        cnt = bin(unc).count("1")
        tot = 0
        for p in unused:
            best = 0
            for c, b in masks[p]:
                v = bin(unc & b).count("1")
                if v > best:
                    best = v
            tot += best
            if tot >= cnt:
                return True
        return tot >= cnt

    def dfs(unc, unused, chosen):
        nodes[0] += 1
        if node_limit and nodes[0] > node_limit:
            raise TimeoutError
        if unc == 0:
            return dict(chosen)
        if not bound(unc, unused):
            return None
        # most constrained uncovered point
        best_i, best_opts = None, None
        x = unc
        while x:
            low = x & -x
            i = low.bit_length()
            opts = [p for p in cover_of[i - 1] if p in unused]
            if best_opts is None or len(opts) < len(best_opts):
                best_i, best_opts = i, opts
                if len(opts) <= 1:
                    break
            x ^= low
        if not best_opts:
            return None
        # try primes covering most uncovered points first
        scored = []
        for p in best_opts:
            c = best_i % p
            b = next(bb for cc, bb in masks[p] if cc == c)
            scored.append((-bin(unc & b).count("1"), p, c, b))
        scored.sort()
        for _, p, c, b in scored:
            unused.remove(p)
            chosen[p] = c
            r = dfs(unc & ~b, unused, chosen)
            if r is not None:
                return r
            del chosen[p]
            unused.add(p)
        return None

    try:
        r = dfs(full, set(odd), {})
    except TimeoutError:
        return None, None
    return (r is not None), r


def check_certificate(k, t, cert):
    """Rebuild n by CRT from the certificate and check the gap directly."""
    m = t // 2
    odd = PR[1:k]
    for i in range(1, m):
        if not any(p in cert and i % p == cert[p] for p in odd):
            return False
    for p, c in cert.items():
        if c % p in (0, m % p):
            return False
    # residues: n + j = 0 (mod p)  <=>  j = 2c (mod p) for odd p, j odd for p = 2
    P = 1
    n = 0
    mods = [(2, 1)]  # n odd -> n+j even for odd j, so n = 1 (mod 2)
    for p in odd:
        c = cert.get(p)
        if c is None:
            c = next(x for x in range(1, p) if x != m % p)
        mods.append((p, (-2 * c) % p))
    for p, r in mods:
        while n % p != r:
            n += P
        P *= p
    import math
    if math.gcd(n, P) != 1 or math.gcd(n + t, P) != 1:
        return False
    return all(math.gcd(n + j, P) > 1 for j in range(1, t))


def gap_set(k, tmax, node_limit=None):
    out = {}
    for t in range(2, tmax + 1, 2):
        ok, cert = gap_occurs(k, t, node_limit)
        if ok:
            assert check_certificate(k, t, cert), (k, t)
        out[t] = ok
    return out


A048670 = [2, 4, 6, 10, 14, 22, 26, 34, 40, 46, 58, 66, 74, 90, 100, 106, 118, 132, 152, 174,
           190, 200, 216, 234, 258, 264, 282, 300, 312, 330, 354, 378, 388, 414, 432, 450, 476,
           492, 510, 538]

if __name__ == "__main__":
    node_limit = 20_000_000
    ks = [int(a) for a in sys.argv[1:]] or list(range(2, 12))
    res = {}
    try:
        res = json.load(open("stage1_gap_sets.json"))
    except Exception:
        pass
    for k in ks:
        t0 = time.time()
        # jac = A048670(k), the maximal gap. For k <= 13 the solver also decides
        # t = jac + 2 (and finds it missing); for larger k it relies on A048670 for
        # t > jac and decides every even t <= jac, which are mostly quick "yes" cases.
        jac = A048670[k - 1]
        tmax = jac + 2 if k <= 13 else jac
        gs = gap_set(k, tmax, node_limit)
        missing = [t for t, v in gs.items() if v is False]
        unknown = [t for t, v in gs.items() if v is None]
        upto = [t for t in missing if t <= jac]
        rec = {"k": k, "p_k": PR[k - 1], "jacobsthal": jac,
               "smallest_missing_even": (min(upto) if upto else jac + 2) if not unknown else None,
               "missing_up_to_max": upto, "unknown": unknown,
               "jac_plus_2_decided_here": k <= 13,
               "seconds": round(time.time() - t0, 1)}
        res[str(k)] = rec
        print(rec, flush=True)
        json.dump(res, open("stage1_gap_sets.json", "w"), indent=1)
