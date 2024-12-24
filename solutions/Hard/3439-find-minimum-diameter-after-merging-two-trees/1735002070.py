class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        #this is kinda messy, but the general idea is to find the most centralized node in each tree, then connect them and find the resulting length.
        #however, there is also an edge case. If either tree already has a diameter of X, then the answer cannot be lower than X
        def findShort(edges):
    
            d = defaultdict(set)
            for u,v in edges:
                d[u].add(v)
                d[v].add(u)
    
            mmap = {}
            dfs(0, mmap, 0, d)
            endpoint = sorted([(-v, k) for k,v in mmap.items()])[0][1]
            mmap2 = {}
            dfs(endpoint, mmap2, 0, d)
            endpoint2 = sorted([(-v, k) for k,v in mmap2.items()])[0][1]
            mmap3 = {}
            dfs(endpoint2, mmap3, 0, d)
            m = len(d.keys())
            best = 1e15
            overall_max = max(max(mmap2.values()), max(mmap3.values()))
            for i in range(m):
                can = max(mmap2[i], mmap3[i])
                best = min(best, can)
            return [best, overall_max]
        
        def dfs(x, mmap, dst, d):
            if x in mmap:
                return
            
            mmap[x] = dst
            for y in d[x]:
                dfs(y, mmap, dst+1, d)
    
        a, o1 = findShort(edges1)
        b, o2 = findShort(edges2)
    
        return max(a+b+1, o1, o2)
    
    
        