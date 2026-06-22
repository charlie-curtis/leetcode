class Solution:
    def maximumLength(self, s: str) -> int:

        C = Counter()
        for t, g in groupby(s):
            l = len(list(g))
            for i in range(l, max(l-3, 0), -1):
                C[(t,i)]+= l-i+1

        return max([k[1] if v>=3 else -1 for k,v in C.items()])
            
            