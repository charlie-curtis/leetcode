class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:

        n = len(stones)

        pre = list(accumulate(stones, initial=0))

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for L in range(n):
            for i in range(n-L):
                j = i+L
                a = pre[j] - pre[i] # take j
                b = pre[j+1] - pre[i+1] #take i
                a-=dp[i][j-1] if j-1 >=0 else 0
                b-=dp[i+1][j] if i + 1 < n else 0
                dp[i][j] = max(a,b)
        return dp[0][n-1]
        




        