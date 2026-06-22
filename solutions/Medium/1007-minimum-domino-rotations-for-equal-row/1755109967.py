class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        n=len(bottoms)
        dpt= [[0 for _ in range(7)] for _ in range(n+1)]
        dpb= [[0 for _ in range(7)] for _ in range(n+1)]

        for i in range(n):
            for j in range(1,7):
                if dpt[i][j] == -1:
                    dpt[i+1][j] = -1
                elif tops[i] == j:
                    dpt[i+1][j] = dpt[i][j]
                elif bottoms[i] == j:
                    dpt[i+1][j] = dpt[i][j]+1
                else:
                    dpt[i+1][j] = -1

                if dpb[i][j] == -1:
                    dpb[i+1][j] = -1
                elif bottoms[i] == j:
                    dpb[i+1][j] = dpb[i][j]
                elif tops[i] == j:
                    dpb[i+1][j] = dpb[i][j]+1
                else:
                    dpb[i+1][j] = -1
        ans=10**9
        for j in range(1,7):
            if dpb[-1][j]!= -1:
                ans=min(ans, dpb[-1][j])
            if dpt[-1][j]!= -1:
                ans=min(ans, dpt[-1][j])
        return ans if ans != 10**9 else -1