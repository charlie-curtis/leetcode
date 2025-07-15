class Solution:
    def minRunesToAdd(self, n: int, crystals: List[int], flowFrom: List[int], flowTo: List[int]) -> int:
        adj = defaultdict(set)
        radj = defaultdict(set)
        for u,v in zip(flowFrom, flowTo):
            adj[u].add(v)
            radj[v].add(u)

        V = [False]*n
        def dfs(u):
            if V[u]:
                return
            #print("visiting", u)
            V[u] = True

            for v in adj[u]:
                dfs(v)

        for u in crystals:
            dfs(u)

        nodes = [i for i in range(n) if not V[i] and len(radj[i]) == 0] #nodes without any incoming vertices.
        ans=len(nodes)
        for u in nodes:
            dfs(u)

        #'finish times' concept from the SCC algo
        FT = [-1]*n
        V2 = [False]*n
        t = 0
        def calc(u):
            nonlocal t
            if V2[u]:
                return
            V2[u] = True
            for v in adj[u]:
                calc(v)
            t+=1
            FT[u] = t

        t = 0
        for i in range(n):
            if not V[i]: calc(i)

        A = sorted([-x,i] for i,x in enumerate(FT))

        #the reason we bothered with finish times and reverse sorting is because we want to make sure
        #we process any SOURCE SCCs first before processing the sink SCCs
        for x,i in A:
            if not V[i]:
                ans+=1
                dfs(i)
        return ans

            

            


        return ans