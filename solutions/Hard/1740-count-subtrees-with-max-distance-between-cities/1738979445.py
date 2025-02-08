class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:


        #editorial

        INF = 10**9
        dst = [[INF]*n for _ in range(n)]
        for u,v in edges:
            u-=1
            v-=1
            dst[u][v] = 1
            dst[v][u] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])
                    dst[j][i] = min(dst[i][j], dst[i][k] + dst[k][j])

        def get(state):

            mmax = 0
            edges = 0
            nodes = 0
            for i in range(n):
                if (state >> i) & 1 == 0:
                    continue
                nodes+=1
                for j in range(i+1,n):
                    if (state >> j) & 1 == 0:
                        continue
                    mmax = max(mmax, dst[i][j])
                    if dst[i][j] == 1:
                        edges+=1
            if edges+1 != nodes:
                return -1
            return mmax



        end = 2**n
        out = [0]*(n-1)
        for state in range(end):
            d = get(state)
            if d > 0:
                out[d-1]+=1
        return out
