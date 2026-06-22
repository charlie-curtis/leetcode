class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        n = len(s)
        out = [0]*n

        for i,x in enumerate(indices):
            out[x] = s[i]
        return ''.join(out)
            
        