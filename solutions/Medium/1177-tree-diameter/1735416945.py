class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def bfs(cur):

            seen = set()
            q = deque()
            q.append([cur, 0])
            seen.add(cur)

            res = []
            while q:
                node, dst = q.popleft()

                res = [node,dst]
                for u in adj[node]:
                    if u not in seen:
                        seen.add(u)
                        q.append([u, dst+1])
            return res


        endpoint = bfs(0)[0]
        return bfs(endpoint)[1]



        