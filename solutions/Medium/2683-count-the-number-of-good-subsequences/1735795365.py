
class Solution:
    def countGoodSubsequences(self, s: str) -> int:

        def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
            max_n = min(max_n, mod - 1)
        
            fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
            fact[0] = 1
            for i in range(max_n):
                fact[i + 1] = fact[i] * (i + 1) % mod
        
            inv_fact[-1] = pow(fact[-1], mod - 2, mod)
            for i in reversed(range(max_n)):
                inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
        
            def nCr_mod(n, r):
                res = 1
                while n or r:
                    a, b = n % mod, r % mod
                    if a < b:
                        return 0
                    res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
                    n //= mod
                    r //= mod
                return res
        
            return nCr_mod


        ncr = make_nCr_mod()


        n = len(s)
        M = 10**9 + 7

        #this problem was hard and i had to look at the editorial. It's all good though because I read up on binomial coefficiens, modular inverses, and
        #I have a better shot at solving this on my own in the future. I was on the right track, somewhat. That's a very loose definition of "right track"


        C = Counter(s)
        mmax = max(C.values())

        ans = 0
        for f in range(1, mmax+1):
            cur = 1
            V = [x for x in C.values() if x>= f]
            for v in V:
                cur*=(1 + ncr(v,f)) #we are adding 1 here because we have the option of not choosing this letter
                cur%=M
            ans+=(cur-1) #we are subtracting 1 here because it previously included the empty subsequence
            ans%=M

        return ans