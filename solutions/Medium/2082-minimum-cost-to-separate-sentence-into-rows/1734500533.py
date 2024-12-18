class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:


        ll = [len(x) for x in sentence.split(" ")]
        pref = list(accumulate(ll, initial = 0))


        n = len(ll)
        INF = 1e15
        @cache
        def dp(i):
            rem = pref[n] - pref[i] + n-i - 1
            if rem <= k:
                #this will be the last line and we can ignore it
                return 0

            cur = 0
            best = INF
            for j in range(i,n):
                cur+=ll[j]
                if cur > k:
                    break
                best = min(best, (k-cur)**2 + dp(j+1))
                cur+=1
            return best

        return dp(0)
            

        