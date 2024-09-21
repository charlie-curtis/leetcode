class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minSeen = 1e10
        ans = 0
        for x in prices:
            minSeen = min(x, minSeen)
            ans = max(ans, x-minSeen)
        return ans

        