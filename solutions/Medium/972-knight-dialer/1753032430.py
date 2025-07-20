class Solution:
    def knightDialer(self, n: int) -> int:


        moves = [
            [4,6], #0
            [6,8], #1
            [7,9], #2
            [4,8], #3
            [3,9,0], #4
            [], #5
            [0,1,7], #6
            [2,6], #7
            [1,3], #8
            [2,4] #9
        ]
        MOD = 10**9 + 7

        dp = [[0 for i in range(10)] for _ in range(n+1)]
        if n == 1:
            return 10
        for i in range(10):
            dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(10):
                for k in moves[j]:
                    dp[i][j]+= dp[i-1][k]
                    dp[i][j]%=MOD
        return sum(dp[-1]) % MOD
