class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = []
        dst = len(graph)-1

        def dfs(i, cur):
            if i == dst:
                cur.append(i)
                ans.append(cur.copy())
                cur.pop()
                return

            cur.append(i)
            for nxt in graph[i]:
                dfs(nxt, cur)
            cur.pop()

        dfs(0, [])

            

        return ans
        