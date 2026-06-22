class Solution:
    def minSteps(self, s: str, t: str) -> int:
        C = Counter(s)
        C2 = Counter(t)

        same = 0
        for k,v in C.items():
            same+=min(C[k], C2[k])

        rem = len(s) - same
        return rem
        