class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        out = [0]*n
        def dfs(cur, p):

            C = Counter()
            for u in adj[cur]:
                if u != p:
                    C+=dfs(u, cur)

            c = labels[cur]
            C[c]+=1
            nonlocal out
            out[cur] = C[c]
            return C
        dfs(0, -1)
        return out
            

                
        