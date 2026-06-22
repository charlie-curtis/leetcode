class Solution:
    def distinctSequences(self, n: int) -> int:


        MOD = 10**9 + 7
        @cache
        def dp(i,one_ago, two_ago):
            if i == n:
                return 1
            
            ans = 0
            for j in range(1,7):
                if one_ago != j and two_ago != j and (one_ago == -1 or gcd(one_ago, j) == 1):
                    ans+=dp(i+1,j,one_ago)
                    ans%=MOD
            
            return ans
        
        return dp(0, -1,-1)

        