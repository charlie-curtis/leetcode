class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:


        n = len(nums)
        dp = [1]*n
        dpL = [1]*n

        for i in range(1,n):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j]+1
                    dpL[i] = dpL[j]
                elif nums[i] > nums[j] and dp[j] + 1 == dp[i]:
                    dpL[i]+=dpL[j]
        mx = max(dp)

        return sum([dpL[i] for i in range(n) if dp[i] == mx])
