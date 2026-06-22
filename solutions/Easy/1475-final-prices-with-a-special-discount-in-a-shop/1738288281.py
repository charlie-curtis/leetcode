class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)

        out = []
        for i in range(n):
            c = 0
            for j in range(i+1,n):
                if prices[i] >= prices[j]:
                    c = prices[j]
                    break
            out.append(prices[i] - c)
        return out