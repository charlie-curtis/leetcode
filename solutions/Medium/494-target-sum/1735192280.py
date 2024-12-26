class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dp(i, b):
            if i == n:
                return 1 if b == target else 0
            return dp(i+1, b - nums[i]) + dp(i+1, b + nums[i])
        
        return dp(0,0)