from collections import Counter


def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x


def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + i) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + i) % n, (y * y + i) % n
                    y = (y * y + i) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)

class Solution:
    def divisibleGame(self, nums: list[int]) -> int:

        factors = [prime_factors(x) for x in nums]
        all_factors = set()
        for C in factors:
            for k in C.keys():
                all_factors.add(k)
        all_factors = sorted(list(all_factors))

        n = len(nums)
        def check(factor):
            A = [0]*(n+1)

            small = 0
            ssum = 0
            best = -10**10
            for x in nums:
                ssum+=(x if x % factor == 0 else -x)
                best = max(best, ssum - small)
                small = min(small, ssum)

            return best


        best = float('-inf')
        if not all_factors:
            #we only pick a single 1. e.g. the input array is like [1,1,1,1,]
            return 1000000005
        for f in all_factors:
            b = check(f)
            if b > best:
                best = b
                k = f

        MOD = 10**9 + 7
        return (best % MOD) * k % MOD
            