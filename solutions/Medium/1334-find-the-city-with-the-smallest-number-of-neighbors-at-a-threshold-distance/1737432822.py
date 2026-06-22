class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:

        
        def dijkstra(graph, start,n):
            """ 
                Uses Dijkstra's algortihm to find the shortest path from node start
                to all other nodes in a directed weighted graph.
            """
            n = len(graph)
            dist, parents = [float("inf")] * n, [-1] * n
            dist[start] = 0
        
            queue = [(0, start)]
            while queue:
                path_len, v = heappop(queue)
                if path_len == dist[v]:
                    for w, edge_len in graph[v]:
                        if edge_len + path_len < dist[w]:
                            dist[w], parents[w] = edge_len + path_len, v
                            heappush(queue, (edge_len + path_len, w))
        
            return dist, parents


        d = defaultdict(set)
        d = [set() for _ in range(n)]
        for u,v,c in edges:
            d[u].add((v,c))
            d[v].add((u,c))

        best = 1e15
        ans = -1
        for i in range(n):
            res = dijkstra(d, i, n)[0]
            cnt = sum([1 if x <= threshold else 0 for x in res])
            if cnt < best:
                ans = i
                best = cnt
            elif cnt == best:
                ans = i
        return ans