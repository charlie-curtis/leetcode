class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:


        n = len(tastiness)

        #dp[i][j][k] - the max tastiness using a prefix [0,i] with a total price of j and k coupons remaining

        dp = [[[0 for _ in range(maxCoupons+1)] for _ in range(maxAmount+1)] for _ in range(n+1)]


        for i in range(1,n+1):
            for j in range(maxAmount+1):
                for k in range(maxCoupons+1):
                    best = dp[i-1][j][k]

                    p = price[i-1]
                    t = tastiness[i-1]
                    #buy without coupon
                    if j-p >= 0:
                        best = max(best, dp[i-1][j-p][k] + t)
                    #buy with coupon
                    if j-p//2 >=0 and k > 0:
                        best = max(best, dp[i-1][j-p//2][k-1] + t)

                    #don't buy
                    best = max(best, dp[i-1][j][k])

                    dp[i][j][k] = best



        #print(dp)
        best = 0
        for i in range(maxAmount+1):
            best = max(best, dp[-1][i][-1])
        return best

