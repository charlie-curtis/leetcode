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
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:


        n = len(s)
        ans = 0
        for K in range(minSize, minSize+1):
            fh = FixedDoubleHash(K, s)
            C = Counter()
            C2 = Counter()
            j = 0
            for i in range(n):

                if i-j+1 > K:
                    fh.drop(j)
                    #subtract
                    C[s[j]]-=1
                    if C[s[j]] == 0:
                        del C[s[j]]
                    j+=1
                #add
                fh.add(i)
                C[s[i]]+=1

                if i-j+1 == K and len(C.keys()) <= maxLetters:
                    #print("hit", s[j:i+1])
                    C2[fh.get()]+=1
                    ans = max(ans, C2[fh.get()])
                    #add hash to C

        return ans
        