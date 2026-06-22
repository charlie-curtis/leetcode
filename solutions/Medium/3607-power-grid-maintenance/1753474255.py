class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        roots = [-1]*c
        graph = [[] for _ in range(c)]
        for u,v in connections:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        

        def dfs(x,root):
            if roots[x] != -1:
                return
            roots[x] = root
            for nxt in graph[x]:
                dfs(nxt, root)
        
        for i in range(c):
            if roots[i] == -1:
                dfs(i, i)

        H = {}
        for i,root in enumerate(roots):
            if root not in H:
                H[root] = SortedList()
            H[root].add(i)
        
        ans = []
        for type, x in queries:
            x-=1
            root = roots[x]
            sl = H[root]
            if type == 1:
                if len(sl) == 0:
                    ans.append(-1)
                elif x in sl:
                    ans.append(x+1)
                else:
                    ans.append(sl[0]+1)
            else:
                if len(sl) > 0:
                    sl.discard(x)
        return ans

