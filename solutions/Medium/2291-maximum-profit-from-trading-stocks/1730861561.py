class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:


        n = len(present)
        dp = [[0 for _ in range(n)] for _ in range(budget+1)]


        for i in range(budget+1):
            for j in range(n):
                if j > 0:
                    dp[i][j] = dp[i][j-1]
                if i-present[j] >= 0:
                    cost = present[j]
                    gain = future[j] -cost
                    prev = dp[i-cost][j-1] if j > 0 else 0
                    dp[i][j] = max(dp[i][j], gain + prev)


        ans = 0
        for i in range(budget+1):
            ans = max(ans, dp[i][-1])
        return ans
