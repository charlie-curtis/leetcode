class ExpandingDoubleHash:
    def __init__(self):
        self.h1 = 0
        self.h2 = 0
        self.MOD1 = 10**9 + 7
        self.MOD2 = 10**9 + 9
        self.m = 0

    def append(self, x):
        self.h1 = self.h1 * 26*31 + x
        self.h2 = self.h2 * 26*31 + x
        self.h1%=self.MOD1
        self.h2%=self.MOD2
        self.m+=1
    def appendleft(self, x):
        self.h1 = self.h1 + pow(26*31, self.m, self.MOD1)*x
        self.h2 = self.h2 + pow(26*31, self.m, self.MOD2)*x
        self.m+=1
        self.h1%=self.MOD1
        self.h2%=self.MOD2
    
    def get(self):
        return (self.h1, self.h2)

class Solution:
    def shortestPalindrome(self, s: str) -> str:

        t = s[::-1]
        n = len(s)
        eh1 = ExpandingDoubleHash()
        eh2 = ExpandingDoubleHash()
        best = 0
        for i in range(n):
            a = ord(s[i])
            b = ord(t[n-1-i])
            eh1.append(a)
            eh2.appendleft(b)
            if eh1.get() == eh2.get():
                best = i+1

        print("best was", best)
        if best == n:
            return s
        addin = s[best:]
        return addin[::-1] + s