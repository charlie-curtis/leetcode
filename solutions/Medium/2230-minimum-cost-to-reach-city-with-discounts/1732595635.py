class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], dis: int) -> int:


        INF = 10**9
        dst = [[INF for _ in range(dis+1)] for _ in range(n)]

        d = defaultdict(list)
        for u,v,w in highways:
            d[u].append([v,w])
            d[v].append([u,w])

        m = len(dst[0])


        def do_dijkstra():
            for i in range(m):
                dst[0][i] = 0

            pq = [(0,0, dis)]

            while pq:
                cost, node, k = heapq.heappop(pq)

                if dst[node][k] < cost:
                    #outdated
                    continue
    
                for u,w in d[node]:
                    if dst[u][k] > w + dst[node][k]:
                        dst[u][k] = w + dst[node][k]
                        heapq.heappush(pq, (w+dst[node][k], u, k))

                    if k-1 >= 0 and dst[u][k-1] > w//2 + dst[node][k]:
                        dst[u][k-1] = w//2 + dst[node][k]
                        heapq.heappush(pq, (w//2+dst[node][k], u, k-1))

        do_dijkstra()
        low = min(dst[n-1])
        return low if low != INF else -1

