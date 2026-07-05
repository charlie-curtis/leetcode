class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        d = defaultdict(list)

        for a,b,x in roads:
            d[a].append(b)
            d[b].append(a)


        
        def dfs(x, seen):
            if x in seen:
                return

            seen.add(x)
            for nxt in d[x]:
                dfs(nxt, seen)

        

        sset = set()
        dfs(1, sset)

        return min([x for (a,b,x) in roads if a in sset or b in sset])