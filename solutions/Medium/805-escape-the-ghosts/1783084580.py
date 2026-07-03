class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        t=target

        
        d1 = min([abs(x-t[0]) + abs(y-t[1]) for (x,y) in ghosts])

        
        d2 = abs(t[0]) + abs(t[1])
        
        return d2 < d1