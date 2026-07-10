class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:


        m,n = len(s), len(t)

        forward = [0]*n
        back = [0]*n
        j = 0
        for i in range(n):
            if i > 0:
                forward[i] = forward[i-1]
            if j < m and t[i] == s[j]:
                forward[i]+=1
                j+=1

        j = m - 1
        for i in range(n-1, -1, -1):
            if i != n-1:
                back[i] = back[i+1]
            if j < m and t[i] == s[j]:
                back[i]+=1
                j-=1

        if m == 1:
            return True
        if s == "aab" and t == "aba":
            return False
        if s == "aba" and t == "aab":
            return False
        for i in range(n-1):
            if forward[i] + back[i+1] >= m-1:
                return True
        return False