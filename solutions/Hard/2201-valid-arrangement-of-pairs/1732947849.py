class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:

        #I failed on this problem for a while because I was just trying to find the start node and then greedy solve it.
        #the actual technique uses eulerian circuits
        n = len(pairs)

        d = defaultdict(deque)
        in_degree = Counter()
        out_degree = Counter()
        for u,v in pairs:
            #directed edge from u -> v
            out_degree[u]+=1
            in_degree[v]+=1
            d[u].append(v)

        root = -1
        for x in out_degree.keys():
            if out_degree[x] - in_degree[x] == 1:
                root = x
                break
        if root == -1:
            root = pairs[0][0]

        
        ans = []
        def dfs(node):
            nonlocal ans

            while len(d[node]) > 0:
                nxt = d[node].pop()
                dfs(nxt)
            
            ans.append(node)


        dfs(root)
        ans = ans[::-1]
        return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]

        
        
