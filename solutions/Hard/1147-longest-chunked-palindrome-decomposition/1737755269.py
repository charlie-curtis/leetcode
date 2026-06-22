class ExpandingDoubleHash:
    def __init__(self):
        self.h1 = 0
        self.h2 = 0
        self.MOD1 = 10**9 + 7
        self.MOD2 = 10**9 + 9
        self.m = 0
        self.flag = 0

    def append(self, x):
        if self.flag not in [0,1]:
            raise ValueError("Do not use both append and appendleft")
        self.flag = 1
        self.h1 = self.h1 * 26*31 + x
        self.h2 = self.h2 * 26*31 + x
        self.h1%=self.MOD1
        self.h2%=self.MOD2
        self.m+=1
    def appendleft(self, x):
        if self.flag not in [0,2]:
            raise ValueError("Do not use both append and appendleft")
        self.flag = 2
        self.h1 = self.h1 + pow(26*31, self.m, self.MOD1)*x
        self.h2 = self.h2 + pow(26*31, self.m, self.MOD2)*x
        self.m+=1
        self.h1%=self.MOD1
        self.h2%=self.MOD2
    
    def get(self):
        return (self.h1, self.h2)
class Solution:
    def longestDecomposition(self, s: str) -> int:


        def dp(i,j):
            if i > j:
                return 0
            if i == j:
                return 1

            eh1 = ExpandingDoubleHash()
            eh2 = ExpandingDoubleHash()
            o = j
            k = i
            MOD = 10**9+7
            while i < j:
                L = o-j
                eh1.append(ord(s[i]))
                eh2.appendleft(ord(s[j]))
                if eh1.get() == eh2.get():
                    return 2 + dp(i+1, j-1)
                i+=1
                j-=1
            return 1
        return dp(0, len(s)-1)