class Solution:
    def checkIfPrerequisite(self, numCourses: int, preqs: List[List[int]], queries: List[List[int]]) -> List[bool]:


        adj = defaultdict(set)

        for u,v in preqs:
            adj[u].add(v)


        @cache
        def dfs(cur, origin, target):

            if cur == target:
                return True
            for u in adj[cur]:
                if dfs(u, origin, target):
                    return True
            return False

        out = []
        for u,v in queries:
            out.append(dfs(u, u,v))
        return out
                

            
            