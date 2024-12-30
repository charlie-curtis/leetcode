class Solution:
    def maxA(self, n: int) -> int:



        @cache
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return -1e30

            a = dp(i-1) + 1
            i-=2
            k = 0
            b = 0
            while i > 0:
                k+=1
                b = max(b,  dp(i)*k)
                i-=1

            return max(a,b)

        return dp(n)
                