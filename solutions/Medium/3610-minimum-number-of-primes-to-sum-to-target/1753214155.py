cutoff = (10000)
P = [True]*(cutoff+1)
P[0] = P[1] = False
i = 2
for i in range(2, int(sqrt(cutoff)) +1):
    if P[i]:
        for j in range(2, int(cutoff//i)+1):
            P[i*j] = False
A = [i for i,x in enumerate(P) if x]
class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:

        L = len(A)
        INF = 10**9
        @cache
        def dp(rem):
            if rem < 0:
                return INF
            if rem == 0:
                return 0

            ans = INF
            for i,x in enumerate(A):
                if i == m:
                    break
                ans = min(ans, dp(rem-x)+1)
            return ans
                
        res = dp(n)
        dp.cache_clear()
        return res if res < INF else -1