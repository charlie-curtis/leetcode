class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:

        m,n = len(g), len(g[0])

        ssum = 0
        seen = []
        for i in range(m):
            for j in range(n):
                ssum+=g[i][j]
            seen.append(ssum)
        
        seen2 = []
        ssum = 0
        for i in range(n):
            for j in range(m):
                ssum+=g[j][i]
            seen2.append(ssum)
        

        T = seen2[-1]
        for x in seen + seen2:
            if 2*x == T:
                return True
        return False

