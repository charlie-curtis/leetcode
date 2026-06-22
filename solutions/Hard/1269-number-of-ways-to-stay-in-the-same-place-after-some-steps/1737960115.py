class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        MOD = 10**9 + 7
        @cache
        def dp(pos, k):
            if pos > k:
                return 0
            if pos < 0 or pos == arrLen:
                return 0
            if k == 0:
                return int(pos==0)


            a = dp(pos-1, k-1)
            b = dp(pos, k-1)
            c = dp(pos+1, k-1)


            return (a+b + c) % MOD
        
        return dp(0, steps)
            

        