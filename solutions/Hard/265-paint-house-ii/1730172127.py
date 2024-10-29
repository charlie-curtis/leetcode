class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        n,k = len(costs), len(costs[0])
        dp = [[0 for _ in range(k)] for _ in range(n)]

        prev = [[1e10, -1], [1e10, -1]]
        for i in range(k):
            dp[0][i] = costs[0][i]
            if dp[0][i] < prev[0][0]:
                prev[1] = prev[0]
                prev[0] = [dp[0][i], i]
            elif dp[0][i] < prev[1][0]:
                prev[1] = [dp[0][i], i]

        if n == 1:
            return min(dp[0])

        for i in range(1, n):
            nxt = [[1e10, -1], [1e10, -1]]
            for j in range(k):
                compat = prev[0][0] if prev[0][1] != j else prev[1][0]
                dp[i][j] = costs[i][j] + compat

                if dp[i][j] < nxt[0][0]:
                    nxt[1] = nxt[0]
                    nxt[0] = [dp[i][j], j]
                elif dp[i][j] < nxt[1][0]:
                    nxt[1] = [dp[i][j], j]
            
            prev = nxt
        
        return min(dp[-1])



