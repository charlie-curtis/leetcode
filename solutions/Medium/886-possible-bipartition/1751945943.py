class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj = defaultdict(set)

        for i,j in dislikes:
            adj[i].add(j)
            adj[j].add(i)

        colors = {}

        def check(i, c):
            if i in colors:
                return colors[i] == c
            
            colors[i] = c
            for nxt in adj[i]:
                if not check(nxt, 1-c):
                    return False
            return True
        for i in range(1,n+1):
            if i not in colors:
                res = check(i, 0)
                if not res:
                    return False
        return True

        
        