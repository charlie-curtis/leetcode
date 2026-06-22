class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dp(i):
            if i == n:
                return 0
            ans = mx = 0
            for j in range(i,min(n,i+k)):
                mx = max(mx, arr[j])
                ans = max(ans, dp(j+1) + mx*(j-i+1))
            return ans
        return dp(0)
        