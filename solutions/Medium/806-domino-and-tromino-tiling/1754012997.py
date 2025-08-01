class Solution:
    def numTilings(self, n: int) -> int:


        #states
        # 0 -> empty
        # 1 -> top filled
        # 2 -> bot filled
        # 3 -> both filled
        MOD = 10**9 + 7
        dp = [[0 for _ in range(4)] for _ in range(n+2)]
        dp[n][0] = 1
        for i in range(n-1,-1,-1):
                dp[i][0] = dp[i+1][0] + dp[i+2][0] + dp[i+1][2] + dp[i+1][1]
                dp[i][0] %=MOD

                dp[i][1] = dp[i+1][2] + dp[i+1][3]
                dp[i][1]%=MOD

                dp[i][2] = dp[i+1][1] + dp[i+1][3]
                dp[i][2] %=MOD

                dp[i][3] = dp[i+1][0]

        return dp[0][0]

'''
top-down
        @cache
        def dp(i,state):
            if i == n:
                return int(state == 0)
            if i > n:
                return 0
            #states
            # 0 -> empty
            # 1 -> top filled
            # 2 -> bot filled
            # 3 -> both filled

            options = []
            if state == 0: #EMPTY
                #place 2x1 vertically
                options.append(dp(i+1, 0))
                #place TWO 2x1 horizontally
                options.append(dp(i+2, 0))
                #place a L
                options.append(dp(i+1, 2))
                #place a 7 rotated 90 degrees counter clockwise
                options.append(dp(i+1, 1))
            elif state == 1: #TOP FILLED
                #place 1 2x1 horizontally on bottom row
                options.append(dp(i+1, 2))
                #place tromino _|
                options.append(dp(i+1, 3))
            elif state == 2: #BOTTOM FILLED
                #place 1 2x1 horizontally on top row
                options.append(dp(i+1, 1))
                #place tromino
                options.append(dp(i+1, 3))
            else:
                options.append(dp(i+1, 0))
                #go to the next row?

            ans = 0
            for x in options:
                ans+=x
                ans%=MOD
            return ans

        return dp(0,0)

'''
        