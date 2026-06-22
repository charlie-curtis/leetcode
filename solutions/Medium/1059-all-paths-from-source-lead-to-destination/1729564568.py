class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        neighbors = defaultdict(set)
        for a,b in edges:
            neighbors[a].add(b)

        if len(neighbors[destination]) > 0:
            return False

        seen = set()
        #make sure there are no cycles
        def dfs(node, backedges):

            if node == destination:
                return True

            if len(neighbors[node]) == 0:
                return False
            
            res = True
            if node in backedges:
                return False
            
            if node in seen:
                return True
            backedges.add(node)
            seen.add(node)
            for nxt in neighbors[node]:
                res&=dfs(nxt, backedges)
            backedges.remove(node)
            return res

        
        backedges = set()
        return dfs(source, backedges)




        