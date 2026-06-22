class Solution:
    def numSub(self, s: str) -> int:

        #1 + 2 + 1 + 2 + 3
        ans = 0
        MOD = 10**9 + 7
        for c,g in groupby(s):
            if c == '0':
                continue
            l = len(list(g))
            ans+=(l*(l+1)//2)
            ans%=MOD
        return ans
            
        