class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        fmap = defaultdict(list)

        for i in range(n-1):
            fmap[i].append(i+1)


        def do_bfs():
            q = deque()
            q.append([0, 0])
            seen = set()
            seen.add(0)
            while q:
                node,dst = q.popleft()
                if node == n-1:
                    return dst

                for u in fmap[node]:
                    if u not in seen:
                        seen.add(u)
                        q.append([u, dst+1])


        ans = []
        for u,v in queries:
            fmap[u].append(v)
            ans.append(do_bfs())
        return ans