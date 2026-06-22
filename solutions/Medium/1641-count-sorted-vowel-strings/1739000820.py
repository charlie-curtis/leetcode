class Solution:
    def countVowelStrings(self, n: int) -> int:

        s = 'aeiou'
        m = len(s)

        @cache
        def dp(x, i):

            if x == 0:
                return 1

            ans = 0
            for j in range(i,m):
                ans+=dp(x-1, j)
            return ans

        return dp(n,0)