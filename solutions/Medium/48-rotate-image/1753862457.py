class Solution:
    def rotate(self, g: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(g)
        for i in range(n):
            for j in range(n):
                if i > j:
                    g[i][j], g[j][i] = g[j][i], g[i][j]
        for i in range(n):
            g[i] = g[i][::-1]
        