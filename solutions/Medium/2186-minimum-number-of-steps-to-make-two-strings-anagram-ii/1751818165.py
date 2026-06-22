class Solution:
    def minSteps(self, s: str, t: str) -> int:

        C1 = Counter(s)
        C2 = Counter(t)
        return sum((C1-C2).values()) + sum((C2-C1).values())
        