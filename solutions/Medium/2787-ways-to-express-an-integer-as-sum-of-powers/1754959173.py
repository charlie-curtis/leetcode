class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        MOD = 10**9 + 7
        @cache
        def dp(y, rem):
            if rem == 0:
                return 1
            if y > rem:
                return 0
            
            ans = dp(y+1, rem) #don't use it at all
            if y**x <= rem:
                ans+=dp(y+1, rem-y**x)
                ans%=MOD
            return ans

        return dp(1, n)
        