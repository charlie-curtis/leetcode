class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_map = {}
        t_map = {}
        n = len(s)
        for i in range(n):
            a = s[i]
            b = t[i]
            if (a in s_map) != (b in t_map):
                #both must be in or both must be out
                return False
            if a not in s_map:
                #both out, so set
                s_map[a] = b
                t_map[b] = a
            if s_map[a] != b or t_map[b] != a:
                #wrong mapping
                return False
        return True
        