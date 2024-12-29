class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = nums[0]**2
        dp[0][1] = nums[0]
        ans = dp[0][0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0] + nums[i], nums[i]**2, dp[i-1][1] + nums[i]**2)
            dp[i][1] = max(dp[i-1][1] + nums[i], nums[i])
            ans = max(ans, dp[i][0])
        return ans
