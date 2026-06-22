class Solution:
    def shortestPathWithHops(self, n: int, tmpEdges: List[List[int]], s: int, d: int, k: int) -> int:

        edges = defaultdict(list)

        for u,v,c in tmpEdges:
            edges[u].append([v, c])
            edges[v].append([u, c])

        
        pq = []
        versioned_distances = [[1e15 for _ in range(k+1)] for _ in range(n)]

        for i in range(k+1):
            versioned_distances[s][i] = 0
        for v,c in edges[s]:
            pq.append([c,v, 0])
            versioned_distances[v][0] = c 
            if k > 0:
                versioned_distances[v][1] = 0 
                pq.append([0,v,1])

        heapq.heapify(pq)

        while pq:
            cost, node, skips_used = heapq.heappop(pq)
            
            if node == d:
                return cost
            
            for u,edge_cost in edges[node]:
                if versioned_distances[u][skips_used] > cost+edge_cost:
                    versioned_distances[u][skips_used] = cost + edge_cost
                    heapq.heappush(pq, [cost+edge_cost, u, skips_used])
                if skips_used < k and versioned_distances[u][skips_used+1] > cost:
                    versioned_distances[u][skips_used+1] = cost
                    heapq.heappush(pq, [cost, u, skips_used+1])
        
        return -1
