class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)
        for u,v,c in edges:
            adj[u].append([v,c])
            adj[v].append([u,c])

        def dijikstra(start):
            q = [(0,start)]
            dsts = [float('inf')] * n
            dsts[start] = 0

            while q:
                cost,node = heapq.heappop(q)
                if dsts[node] < cost:
                    #could be outdated
                    continue
            
                for nxt,nc in adj[node]:
                    if dsts[nxt] > nc+cost:
                        dsts[nxt] = nc+cost
                        heapq.heappush(q, [nc+cost, nxt])
            return dsts

        A = dijikstra(0)
        B = dijikstra(n-1)

        T = A[-1]

        ans = []
        for u,v,c in edges:
            if B[v] > B[u]:
                #make v closer to the end node
                u,v = v,u
            if T == float('inf'):
                ans.append(False)
            else:
                ans.append(A[u] + B[v] + c == T)
        return ans