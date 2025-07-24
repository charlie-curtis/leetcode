class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:

        n = len(nums)
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        #arbitrarily root the tree

        #compute the xors of the nodes below you

        #then, iterate through every combination of edge (1000 pick 2 passes)

        #case 1. The two edges chosen aren't in the same subtree
        #the three xors would then be xor(subtree of A), xor (subtree of B)
        #and then the last would be xor(total) ^ (values from above)

        #those would be the 3 xor values, then we can find the min/max of those.

        #case 2. the edges we pick lie in the same subtree

        '''
            A
          B  F
          C
          D
          E

          say we pick edges (CD) and (AB)
          xor1 = xor(D)
          xor2 = xor(B^D)
          xor 3 = total ^ (results from above)
          how do we find if the lie in the same subtree? LCA?

        '''
        depths = [[0 for _ in range(n)] for _ in range(n)]
        xors = [[0 for _ in range(n)] for _ in range(n)]
        start_time = [0]*n
        end_time = [0]*n

        t = 0
        def dfs(node, prev):
            nonlocal t
            t+=1
            start_time[node] = t
            xor = nums[node]
            for nxt in graph[node]:
                if nxt != prev:
                    xor^=dfs(nxt, node)
            xors[node] = xor
            end_time[node] = t
            return xor

        dfs(0, -1)
        m = len(edges)
        ans = float('inf') 
        def is_subtree(B,D):
            return start_time[B] <= start_time[D] and end_time[B] >= end_time[D]
        for i in range(m):
            for j in range(i+1, m):
                A,B = edges[i]
                C,D = edges[j]
                #make B and D always the child (closer to the leaves)
                if start_time[A] > start_time[B]:
                    A,B = B,A
                if start_time[C] > start_time[D]:
                    C,D = D,C
                xor1 = xors[B]
                xor2 = xors[D]
                if is_subtree(B,D) or is_subtree(D,B):
                    if start_time[B] > start_time[D]:
                        xor2^=xor1
                    else:
                        xor1^=xor2
                xor3 = xors[0]^xor1^xor2
                a = max([xor3,xor2,xor1]) - min([xor3,xor2,xor1])
                ans = min(ans, max([xor3,xor2,xor1]) - min([xor3,xor2,xor1]))
        return ans






        