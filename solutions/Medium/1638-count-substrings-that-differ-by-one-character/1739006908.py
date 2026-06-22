class Solution:
    def countSubstrings(self, s: str, t: str) -> int:


        m,n = len(s), len(t)

        ans = 0
        for i in range(m):
            for j in range(n):
                diff = 0
                u,v = i,j
                while u < m and v < n and diff < 2:
                    if s[u] != t[v]:
                        diff+=1
                    if diff == 1:
                        ans+=1
                    u+=1
                    v+=1
        return ans
                    