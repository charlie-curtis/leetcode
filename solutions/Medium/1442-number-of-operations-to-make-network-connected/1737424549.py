class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        adj = defaultdict(set)
        for a,b in connections:
            adj[a].add(b)
            adj[b].add(a)

        seen = set()
        def dfs(cur):
            if cur in seen:
                return
            seen.add(cur)
            for nxt in adj[cur]:
                dfs(nxt)

        cnt = 0
        for i in range(n):
            if i not in seen:
                cnt+=1
                dfs(i)

        if cnt == 1:
            return 0
        #you have to have atleast n-1 edges
        edges = len(connections)
        if edges >= n-1:
            return cnt-1
        return -1