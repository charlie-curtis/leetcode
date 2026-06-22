class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1

        out = [-1]*(n-k+1)
        for i in range(n-k+1):
            if dp[i+k-1] - dp[i] == k-1:
                out[i] = nums[i+k-1]
        return out
