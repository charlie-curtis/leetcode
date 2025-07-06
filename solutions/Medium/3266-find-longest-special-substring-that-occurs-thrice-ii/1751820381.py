class Solution:
    def maximumLength(self, s: str) -> int:

        C = Counter()
        for c, g in groupby(s):
            l = len(list(g))
            for t in range(l, max(0, l-3), -1):
                C[(c,t)]+=(l-t)+1 
        return max([-1 if v < 3 else k[1] for k,v in C.items()])

        