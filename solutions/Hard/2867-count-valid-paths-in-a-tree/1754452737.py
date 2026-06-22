cutoff = 10**5
P = [True]*(cutoff+1)
P[0] = P[1] = False

i = 2
while i*i <= cutoff:
    if P[i]:
        for j in range(2, cutoff//i+1):
            P[i*j] = False
    i+=1
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:

        #partial editorial

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        ans = 0
        def dfs(node, prev):
            nonlocal ans
            #there is specific ordering for multiplying these paths together. I had the general idea, but the ordering of things I messed up a bit.
            if P[node]:
                paths = [0,1]
            else:
                paths = [1,0]
            for x in adj[node]:
                if x == prev:
                    continue
                np, p = dfs(x, node)
                ans+= paths[0]*p
                ans+= paths[1]*np
                if P[node]:
                    paths[1]+=np
                else:
                    paths[0]+=np
                    paths[1]+=p
            return paths
            
        dfs(1, -1)
        return ans