class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:


        m,n = len(matrix), len(matrix[0])

        @cache
        def dp(i,j):
            if i == m:
                return 0
            if j < 0 or j == n:
                return 10**9
            
            return min(dp(i+1,j), dp(i+1, j-1), dp(i+1, j+1)) +  matrix[i][j]
            
        
        return min([dp(0, j) for j in range(n)])
        