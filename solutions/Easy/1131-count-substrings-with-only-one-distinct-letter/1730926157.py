class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        for _, g in groupby(s):
            n = len(list(g))
            ans+=n*(n+1)//2
        return ans