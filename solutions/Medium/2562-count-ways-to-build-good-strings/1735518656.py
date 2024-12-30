class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:


        M = 10**9 + 7
        @cache
        def dp(l):
            if l == 0:
                return 1
            if l < 0:
                return 0
            a = dp(l-zero) % M
            b = dp(l - one) % M
            return (a + b) % M

        ans = 0
        for x in range(low, high+1):
            ans+=dp(x)
            ans%=M
        return ans
        