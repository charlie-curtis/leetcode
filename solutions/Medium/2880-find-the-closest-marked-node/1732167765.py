class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:

        tmp = edges
        marked = set(marked)
        edges = defaultdict(list)
        for u,v,w in tmp:
            edges[u].append([v,w])


        dst = [float('inf') for _ in range(n)]

        dst[s] = 0
        q = [[0,s]]

        if s in marked:
            return 0

        while q:
            cost, node = heapq.heappop(q)

            if cost != dst[node]:
                #something else has already updated it
                continue

            if node in marked:
                return dst[node]

            for u,w in edges[node]:
                if dst[u] > dst[node] + w:
                    dst[u] = dst[node] + w
                    heapq.heappush(q, [dst[u], u])
        return -1
        