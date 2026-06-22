class Solution:
    def maxTotalReward(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        nums.sort()

        ans = 0
        mx = nums[-1]
        dp = [[False for _ in range(mx+1)] for _ in range(n+1)]
        dp[0][0] = True

        #dp[i][j] = i is the prefix of nums we're considering,
        #j is the value
        for i in range(n):
            for j in range(mx+1):
                dp[i+1][j] = dp[i][j]
            for j in range(mx+1):
                if j >= nums[i]:
                    break
                if dp[i][j]:
                    ans = max(j+nums[i], ans)
                    if j+nums[i] < len(dp[i+1]):
                        dp[i+1][j+nums[i]] = True
        return ans