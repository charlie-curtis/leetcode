class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        MOD = 10**9 + 7
        @cache
        def dp(i, rem):
            if i == n:
                return int(rem == 0)
            if rem < 0:
                return 0
            
            ans = 0
            for j in range(1,k+1):
                ans+=dp(i+1, rem-j)
                ans%=MOD
            return ans
        
        return dp(0,target) % MOD




        