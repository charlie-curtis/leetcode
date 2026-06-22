class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])

        q = [[0,k]]

        seen = set()
        while q:
            t, node = heapq.heappop(q)

            if node in seen:
                continue
            seen.add(node)
            if len(seen) == n:
                return t

            for nxt,w in adj[node]:
                heapq.heappush(q, [t+w, nxt])
        
        return -1
            