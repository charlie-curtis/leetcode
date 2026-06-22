class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:


        MOD = 10**9 + 7
        n = len(s)
        @cache
        def dp(i):
            if i == n:
                return 1

            ans = 0
            v =0 
            for j in range(i,n):
                v = v * 10 + int(s[j])
                if 1<= v <= k and (j+1 == n or s[j+1] != '0'):
                    ans+=dp(j+1)
                    ans%=MOD
                if v > k:
                    break
            return ans
        return dp(0)
                    
        