class Solution:
    def numSquares(self, n: int) -> int:

        #is greedy always the best approach? No. 
        #12 = 4 + 4 + 4 = 3 moves
        #12 = 9 + 1 + 1 + 1 = 4 moves
        #sqrt(n)*n = n^(3/2) -> does that pass? maybe

        #algorithm = iterate bottom up DP. At each value, see if every perfect square could improve your answer
        cut = int(sqrt(n))
        dp = [10**9 for _ in range(n+1)]
        dp[0] = 0

        for sq in range(1, cut+1):
            V = sq*sq
            for y in range(1, n+1):
                if y-V >= 0:
                    dp[y] = min(dp[y], 1 + dp[y-V])
        return dp[n]