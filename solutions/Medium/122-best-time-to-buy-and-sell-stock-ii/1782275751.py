class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        prev_has = has = -1e10
        prev_dont = dont = 0

        for i in range(n):
            dont = prev_dont
            has = prev_has

            #to not have stock, you can sell it if you had it previously
            dont = max(dont, has + prices[i])
            #to have stock, you can buy it if you didn't previously have it
            has = max(has, dont - prices[i])

            prev_has, prev_dont = has, dont

        return dont