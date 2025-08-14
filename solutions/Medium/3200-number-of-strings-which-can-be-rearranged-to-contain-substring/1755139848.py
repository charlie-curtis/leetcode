class Solution:
    def stringCount(self, n: int) -> int:


        MOD = 10**9 + 7


        @cache
        def dp(i, used):
            if i == n:
                return int(used == 2**4-1)
            
            ans = dp(i+1, used)*23
            ans%=MOD
            #L
            ans+=dp(i+1, used|(1<<3))
            ans%=MOD
            #E
            if used&(1<<2):
                ans+=dp(i+1, used|(1<<1))
            else:
                ans+=dp(i+1, used|(1<<2))
            ans%=MOD
            #T
            ans+=dp(i+1, used|1)
            ans%=MOD
            return ans
        return dp(0, 0)
        