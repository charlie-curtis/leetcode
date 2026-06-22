class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adj = defaultdict(set)
        for i,(a,b) in enumerate(edges):
            p = succProb[i]
            adj[a].add((b,p))
            adj[b].add((a,p))
            

        dst = [0]*n
        dst[start] = 1
        pq = [[1, start]]

        while pq:
            p1, node = heappop(pq)
            p1 = abs(p1)
            if node == end:
                return p1

            if dst[node] > p1:
                continue

            for u,p2 in adj[node]:
                if dst[u] < p2*p1:
                    dst[u] = p2*p1
                    heappush(pq, [-p2*p1, u])
        return 0
        