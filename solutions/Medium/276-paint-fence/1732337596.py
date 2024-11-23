class Solution:
    def numWays(self, n: int, k: int) -> int:


        @cache
        def dp(i, rem):
            if i == n:
                return 1

            ans = (k-1)*(dp(i+1, 1))

            if rem > 0:
                ans+=dp(i+1, rem-1)

            return ans

        return dp(0, 2)


        