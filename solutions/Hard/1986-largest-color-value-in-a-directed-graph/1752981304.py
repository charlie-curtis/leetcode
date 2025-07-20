class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:


        m,n = len(colors), len(edges)
        adj = defaultdict(set)
        radj = defaultdict(set)

        C = Counter()
        for u,v in edges:
            adj[v].add(u)
            radj[u].add(v)
            C[u]+=1

        q = []
        cnts = [Counter() for i in range(m)]
        for i in range(m):
            if C[i] == 0:
                q.append(i)
                cnts[i][colors[i]] = 1

        while q:
            node = q.pop()
            for nxt in adj[node]:
                C[nxt]-=1
                if C[nxt] == 0:
                    q.append(nxt)
                    for j in range(26):
                        c = chr(j+ord('a'))
                        mx = 0
                        for tmpu in radj[nxt]:
                            mx = max(mx, cnts[tmpu][c])
                        cnts[nxt][c] = mx
                    cnts[nxt][colors[nxt]]+=1
        
        if sum(C.values()) != 0:
            return -1
        best = 0
        return max([max(x.values()) for x in cnts])
        for i in range(m):
            C = cnts[i]
            if C.values():
                best = max(best, max(C.values()))
        return best