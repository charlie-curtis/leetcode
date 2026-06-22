class FixedDoubleHash:
    def __init__(self, windowSize, content):
        self.h1 = 0
        self.h2 = 0
        self.m = windowSize
        self.s = content
        self.MOD1 = 10**9 + 7
        self.MOD2 = 10**9 + 9

    def drop(self,i):
        self.h1 -= pow(26*31, self.m-1, self.MOD1)*ord(self.s[i])
        self.h2 -= pow(26*31, self.m-1, self.MOD2)*ord(self.s[i])
        self.h1%=self.MOD1
        self.h2%=self.MOD2

    def add(self, i):
        self.h1 = self.h1 * 26*31 + ord(self.s[i])
        self.h2 = self.h2 * 26*31 + ord(self.s[i])
        self.h1%=self.MOD1
        self.h2%=self.MOD2
    
    def get(self):
        return (self.h1, self.h2)
class Solution:
    def longestDupSubstring(self, s: str) -> str:

        n = len(s)
        l = 0
        r = n-1

        ans = ""
        def check(mid):
            nonlocal ans
            dh1 = FixedDoubleHash(mid, s)
            C = Counter()
            for i in range(n):
                if i - mid >= 0:
                    dh1.drop(i-mid)
                dh1.add(i)
                if i >= mid-1:
                    if C[dh1.get()] >= 1:
                        if len(ans) < mid:
                            ans = s[i-mid+1:i+1]
                        return True
                    C[dh1.get()]+=1
            return False

        #TTTTFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1
        return ans
        