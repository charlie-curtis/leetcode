class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:


        adj = defaultdict(set)
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)


        def dfs(node, target, cur):
            nonlocal path


            if node in cur:
                return
            cur.add(node)

            if node == target:
                path = cur.copy()
                return
                
            for u in adj[node]:
                if u not in cur:
                    dfs(u, target, cur)

            cur.remove(node)

        def bfs(path, target):
            if target in path:
                return target
            seen = path.copy()
            q = deque([(x,x) for x in path])
            while q:
                node, origin = q.popleft()
                if node == target:
                    return origin
                for nxt in adj[node]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, origin))


        m = len(query)
        ans = []
        for start,end, target in query:
            path = set()
            dfs(start,end, set())
            ans.append(bfs(path, target))
        return ans

