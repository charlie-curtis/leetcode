class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        nei = defaultdict(list)
        for u,v in edges:
            nei[u].append(v)
            nei[v].append(u)
        
        dst = defaultdict(int)

        def dfs(node, l, prev, dst):

            dst[node] = l
            for u in nei[node]:
                if u != prev:
                    dfs(u, l+1, node, dst)
        

        dfs(0, 0, -1, dst)

        bob_times = {}
        def dfs_bob(node, prev, t):

            nonlocal bob_times
            bob_times[node] = t
            small = min([dst[v] for v in nei[node]])
            for v in nei[node]:
                if dst[v] == small and v != prev:
                    dfs_bob(v, node, t+1)
            pass
        
        dfs_bob(bob, -1, 0)

        ans = -1e20
        def dfs2(node, score, prev, t):

            nonlocal ans
            is_leaf = len(nei[node]) == 1 and node != 0
            multi = 1
            if node in bob_times and t > bob_times[node]:
                multi = 0
            if node in bob_times and t == bob_times[node]:
                multi/=2
            
            score+= amount[node]*multi
            if is_leaf:
                ans = max(ans, int(score))
            else:
                for u in nei[node]:
                    if u != prev:
                        dfs2(u, score, node, t+1)


        dfs2(0, 0, -1, 0)
        return ans
        return -1
