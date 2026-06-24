class Solution:
    def numDecodings(self, s: str) -> int:


        n = len(s)

        @cache
        def f(x):
            if x >= n:
                return 1
            ans = 0
            cur = 0
            for j in range(x,n):
                cur = 10*cur + int(s[j])
                if 1 <= cur <= 26:
                    ans+=f(j+1)
                else:
                    break
            return ans

        return f(0)
        