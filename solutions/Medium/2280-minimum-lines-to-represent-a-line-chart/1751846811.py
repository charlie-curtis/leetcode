class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)

        if n == 1: return 0
        if n == 2: return 1

        stockPrices.sort()
        def getSlope(i):
            num = stockPrices[i][1] - stockPrices[i-1][1]
            den = (stockPrices[i][0] - stockPrices[i-1][0])
            t = gcd(num, den)
            return (num//t, den//t)

        prev = getSlope(1)
        ans = 1
        for i in range(2,n):
            cur = getSlope(i)
            if prev != cur:
                ans+=1
            prev = cur
        return ans


        