class Solution:
    def countOrders(self, n: int) -> int:


        MOD = 10**9 + 7
        @cache
        def dp(p, d):
            if p == n and d == n:
                return 1

            ans = 0
            if p < n:
                #we can either pickup an item
                a = dp(p+1, d)* (n-p)
                ans+=a
                ans%=MOD
            if p > d:
                #or we can deliver any of the items previously picked up
                a = dp(p, d+1)*(p-d)
                ans+=a
                ans%=MOD

            return ans

        return dp(0,0)
                
                
        