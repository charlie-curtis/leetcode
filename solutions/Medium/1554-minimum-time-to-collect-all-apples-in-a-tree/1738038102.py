class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur, p):


            ans = 0 
            for u in adj[cur]:
                if u != p:
                    ans+=dfs(u, cur)

            if ans == 0 and not hasApple[cur]:
                return 0

            if cur != 0:
                ans+=2
            return ans
        return dfs(0, -1)