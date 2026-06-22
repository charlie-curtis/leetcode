class Solution:
    def longestPrefix(self, s: str) -> str:

        n = len(s)
        h1 = h2 = 0
        ans = -1 
        MOD = 10**9 + 7
        for i in range(n):
            c, c2 = ord(s[i]), ord(s[n-1-i])
            h1 = (h1*26*31 + ord(s[i])) % MOD
            h2+= c2*pow(26*31, i, MOD)
            h2%=MOD
            if h1 == h2 and i != n-1:
                ans = i
        return s[:ans+1]