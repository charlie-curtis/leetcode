class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10**9 + 7
        @cache
        def dp(i, used, mmax):
            if i == n:
                return int(used == k)
            if used > k:
                return 0

            ans = 0
            for j in range(1,m+1):
                ans+=dp(i+1, used+1 if j > mmax else used, max(mmax, j))
                ans%=MOD
            return ans

        return dp(0, 0, 0)
                
        