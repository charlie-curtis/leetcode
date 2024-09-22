class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def can_add(s, t):
            if len(t) - len(s) != 1:
                return False
            bad_idx = -1
            for i in range(len(s)):
                if s[i] != t[i]:
                    bad_idx = i
                    break
            
            return bad_idx == -1 or ((t[:bad_idx] + t[bad_idx+1:]) == s)

        def can_replace(s,t):
            n = len(t)
            if len(s) != len(t):
                return False
            wrongs = 0
            for i in range(n):
                if s[i] != t[i]:
                    wrongs+=1
            return wrongs == 1

        return can_add(s,t) or can_add(t,s) or can_replace(s,t)
        