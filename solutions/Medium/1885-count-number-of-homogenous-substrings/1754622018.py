class Solution:
    def countHomogenous(self, s: str) -> int:

        ans = 0
        MOD = 10**9 + 7

        for _, g in groupby(s):
            n = len(list(g))
            ans+=n*(n+1)//2
            ans%=MOD
        return ans
        