class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        n = len(s)
        l = Counter()
        r = Counter(s[1:])
        seen = set()
        for i in range(1,n-1):
            x = s[i]
            r[x]-=1
            l[s[i-1]]+=1
            for y in r.keys():
                if l[y] > 0 and r[y] > 0:
                    seen.add(y+x+y)
        return len(seen)
        