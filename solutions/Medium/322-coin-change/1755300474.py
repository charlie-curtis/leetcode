class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        @cache
        def dp(x):
            if x == 0:
                return 0
            if x < 0:
                return float('inf')
            
            ans = float('inf')
            for y in coins:
                ans = min(ans, dp(x-y) + 1)
            return ans

        res = dp(amount)
        return res if res != float('inf') else -1