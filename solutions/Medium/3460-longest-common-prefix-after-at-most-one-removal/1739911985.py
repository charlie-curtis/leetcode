class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:

        m,n = len(s), len(t)

        ans = 0
        i,j = 0,0
        while i < m and j < n:
            if s[i] != t[j]:
                if i != j:
                    break
                i+=1
                continue
            i+=1
            j+=1
        return j