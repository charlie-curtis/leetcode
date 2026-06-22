class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:


        q = [(0,0)]
        dsts = [float('inf')] * n
        ways = [1] + [0]*(n-1)
        MOD = 10**9 + 7

        adj = defaultdict(list)
        for u,v,c in roads:
            adj[u].append([v,c])
            adj[v].append([u,c])

        while q:
            cost,node = heapq.heappop(q)
            if dsts[node] < cost:
                #could be outdated
                continue
            
            if node == n-1:
                break

            for nxt,nc in adj[node]:
                if dsts[nxt] > nc+cost:
                    ways[nxt] = ways[node]
                    dsts[nxt] = nc+cost
                    heapq.heappush(q, [nc+cost, nxt])
                elif dsts[nxt] == nc+cost:
                    ways[nxt]+=ways[node]
                    ways[nxt]%=MOD
        
        return ways[n-1]