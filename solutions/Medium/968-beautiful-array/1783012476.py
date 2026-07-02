class Solution:
    def beautifulArray(self, n: int) -> List[int]:

        out = [1,2]
        while len(out) < n:
            out = [2*x for x in out] + [2*x -1 for x in out]
        
        return [x for x in out if x <= n]

