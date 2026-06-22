class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:

        edges = defaultdict(list)

        for a,b,c in roads:
            edges[a-1].append([b-1,c])
            edges[b-1].append([a-1,c])

        def dijkstra(start):

            pq = [[0, start]]
            ans = appleCost[i]

            dsts = [float('inf')]*n

            while pq:
                cost, node = heapq.heappop(pq)
                if cost > dsts[node]:
                    continue
                ans = min(ans, cost + appleCost[node])

                for nxt,c1 in edges[node]:
                    nxt_cost = cost + c1 + k*c1
                    if nxt_cost >= dsts[nxt]:
                        continue
                    dsts[node] = cost
                    heapq.heappush(pq, [cost + c1 + k*c1, nxt])


            return ans

        out = []
        for i in range(n):
            out.append(dijkstra(i))
        return out
        