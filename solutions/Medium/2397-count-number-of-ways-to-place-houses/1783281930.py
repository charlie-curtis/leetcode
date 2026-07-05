class Solution:
    def countHousePlacements(self, n: int) -> int:

        MOD=10**9 + 7

        @cache
        def dp(i):
            if i >= n:
                return 1

            a = dp(i+1)
            b = dp(i+2)
            return (a + b) % MOD

        return (dp(0)*dp(0)) % MOD
            
        