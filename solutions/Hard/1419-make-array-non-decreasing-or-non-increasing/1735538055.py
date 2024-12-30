class Solution:
    def convertArray(self, nums: List[int]) -> int:

        def dp(A):
            INF = 10**9 + 7
            m,n = 1001, len(A)
            dp = [[0 for _ in range(m)] for _ in range(n)]
    
            for i in range(m):
                if A[0] > i:
                    dp[0][i] = abs(A[0] - i)
                else:
                    dp[0][i] = 0
    
            
            for i in range(1,n):
                for j in range(m):
                    #this will produce a valid sequence
                    dp[i][j] = dp[i-1][j] + abs(A[i] - j)

                    if j:
                        dp[i][j] = min(dp[i][j], dp[i][j-1])
                
    
            return min(dp[-1])
        
        a = dp(nums)
        b = dp(nums[::-1])
        return min(a,b)