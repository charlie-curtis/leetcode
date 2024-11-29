class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        seen = set()
        d = defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)

        def dfs(node):

            if node in seen:
                return
            
            seen.add(node)
            for x in d[node]:
                dfs(x)



        ans = 0
        for i in range(n):
            if i not in seen:
                ans+=1
                dfs(i)
        return ans


        