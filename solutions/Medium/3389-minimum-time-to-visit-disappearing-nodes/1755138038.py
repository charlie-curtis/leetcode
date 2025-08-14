class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

        adj = defaultdict(list)

        edges.sort(key= lambda x: x[2])
        seen = set()
        for u,v,w in edges:
            u,v = min(u,v), max(u,v)
            if (u,v) in seen:
                continue
            seen.add((u,v))
            adj[u].append([v,w])
            adj[v].append([u,w])

        dsts = [float('inf')]*n
        dsts[0] = 0
        pq = [[0,0]]

        while pq:
            t, node = heapq.heappop(pq)
            if dsts[node] < t:
                continue
            for nxt,w in adj[node]:
                if t+w >= disappear[nxt] or dsts[nxt] <= t+w:
                    continue
                dsts[nxt] = t+w
                heapq.heappush(pq, [t+w, nxt])
        
        dsts = [x if x != float('inf') else -1 for x in dsts]
        return dsts
            