class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:

        adj = defaultdict(set)
        costs = defaultdict(int)
        for u,v,c in edges:
            adj[u].add((v))
            adj[v].add((u))
            costs[(v,u)] = c
            costs[(u,v)] = c

        
        n = len(edges)+1
        dsts = [0]*n
        pref = [0]*n

        def init_dfs(u,p, cur, ssum):
            dsts[u] = cur
            pref[u] = ssum
            for v in adj[u]:
                t = costs[(u,v)]
                if v != p:
                    init_dfs(v, u, cur+1, ssum+t)
        
        init_dfs(0,-1, 1, 0)

        #max length, min # of nodes
        best = [0, 1e15]
        def dfs(u, p, d, last_bad, first_good):
            nonlocal best

            me = nums[u]
            if me in d:
                if last_bad == -1 or dsts[last_bad] < dsts[d[me][0]]:
                    last_bad, first_good = d[me]

            L = pref[u] - (0 if first_good == -1 else pref[first_good])
            D = dsts[u] - (0 if first_good == -1 else dsts[last_bad])

            if L > best[0]:
                best = [L, D]
            elif L == best[0]:
                best[1] = min(best[1], D)


            for v in adj[u]:
                #store the last bad index we saw and the starting idx
                prev = None
                if me in d:
                    prev = d[me]
                d[me] = [u,v]
                if v != p:
                    dfs(v, u, d,last_bad, first_good)
                if prev:
                    d[me] = prev
                else:
                    del d[me]

        dfs(0, -1, {}, -1, -1)
        return best