class FixedDoubleHash:
    def __init__(self, windowSize, content):
        self.h1 = 0
        self.h2 = 0
        self.m = windowSize
        self.s = content
        self.MOD1 = 10**9 + 7
        self.MOD2 = 10**9 + 9

    #WHEN COLLAPSING WINDOW, DROP BEFORE YOU ADD
    def drop(self,i):
        self.h1 -= pow(26*31, self.m-1, self.MOD1)*ord(self.s[i])
        self.h1%=self.MOD1

    def add(self, i):
        self.h1 = self.h1 * 26*31 + ord(self.s[i])
        self.h1%=self.MOD1
    
    def get(self):
        return self.h1
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:

        patterns = p.split("*")
        f = []
        patterns = [p for p in patterns if p]
        if not patterns:
            return 0

        locs = [[] for _ in range(len(patterns))]
        for i,p in enumerate(patterns):
            tmp = FixedDoubleHash(len(p), p)
            for j in range(len(p)):
                tmp.add(j)
            goal = tmp.get()
            tmp = FixedDoubleHash(len(p), s)
            k = 0
            for j in range(len(s)):
                if j - k +1 > len(p):
                    tmp.drop(k)
                    k+=1
                tmp.add(j)
                if tmp.get() == goal:
                    locs[i].append(k)

        
        m = len(locs)
        #print(locs)
        ptrs = [0]*m
        ans = 1e15
        p1 = p2 = 0
        #print(patterns)
        for i in range(len(locs[0])):

            j = locs[0][i]
            start = j
            if m == 1:
                return len(patterns[0])
            j+=len(patterns[0])
            while p1 < len(locs[1]) and locs[1][p1] < j:
                p1+=1
            if p1 < len(locs[1]):
                j = locs[1][p1] + len(patterns[1])
                if m == 2:
                    ans = min(ans, j-start)
                    continue
                while p2 < len(locs[2]) and locs[2][p2] < j:
                    p2+=1
                if p2 < len(locs[2]):
                    j = locs[2][p2] + len(patterns[2])
                    ans = min(ans, j-start)
        return ans if ans < 1e15 else -1
