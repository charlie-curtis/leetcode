class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        d = defaultdict(list)

        for a,b,cost in connections:
            d[a-1].append([cost, b-1])
            d[b-1].append([cost, a-1])


        pq = d[0]
        heapq.heapify(pq)
        
        seen = set([0])
        ans = 0
        while len(seen) != n and pq:
            cost, node = heapq.heappop(pq)
            if node in seen:
                continue
            
            ans+=cost
            seen.add(node)
            for cost, nxt in d[node]:
                if nxt in seen:
                    continue
                heapq.heappush(pq, [cost,nxt])

        
        if len(seen) == n:
            return ans
        return -1



