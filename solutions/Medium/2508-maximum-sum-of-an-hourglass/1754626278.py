class Solution:
    def maxSum(self, g: List[List[int]]) -> int:

        m,n = len(g), len(g[0])

        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                can = g[i][j] + g[i+2][j] + g[i][j+1] + g[i][j+2] + g[i+1][j+1] + g[i+2][j+1] + g[i+2][j+2]
                ans = max(can, ans)
        return ans
        