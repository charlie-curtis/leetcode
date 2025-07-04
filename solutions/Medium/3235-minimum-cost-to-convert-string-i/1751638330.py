class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        INF = 1e20
        V = [[INF for _ in range(26)] for _ in range(26)]

        for i in range(26):
            V[i][i] = 0
        for x,y,c in zip(original, changed, cost):
            x,y = ord(x) - ord('a'), ord(y) - ord('a')
            V[x][y] = min(V[x][y], c)
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    V[i][j] = min(V[i][j], V[i][k] + V[k][j])
        ans = 0
        for s,t in zip(source,target):
            x,y = ord(s) - ord('a'), ord(t) - ord('a')
            ans+=V[x][y]
        
        if ans >= INF:
            return -1
        return ans