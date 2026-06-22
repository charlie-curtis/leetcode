class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        p1, p2 = p.split("*")

        l, r = s.find(p1), s.rfind(p2)

        if l == -1 or r == -1:
            return False
        return r-l >= len(p1)