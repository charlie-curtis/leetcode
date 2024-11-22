class Solution:
    def maxEqualRowsAfterFlips(self, grid: List[List[int]]) -> int:


        m,n = len(grid), len(grid[0])

        def strXor(s):
            out = ''.join(['1' if x == '0' else '0' for x in s])
            return out

        C = Counter()
        ans = 0
        for i in range(m):
            can = ''.join([str(x) for x in grid[i]])
            C[can]+=1
            comp = strXor(can)
            ans = max(ans, C[can] + C[comp])

        return ans