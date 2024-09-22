class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        A = s.split()
        m1 = {}
        m2 = {}

        if len(A) != len(p):
            return False
        for i,a in enumerate(p):
            w = A[i]
            if (a in m1) != (w in m2):
                return False
            if a not in m1:
                m1[a] = w
                m2[w] = a
            if m1[a] != w or m2[w] != a:
                return False
        return True


        