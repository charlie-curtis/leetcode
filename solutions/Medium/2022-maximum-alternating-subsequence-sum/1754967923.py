class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:



        n = len(nums)
        @cache
        def dp(i, add):
            if i == n:
                return 0
            
            a = dp(i+1, add)
            b = dp(i+1, not add) + (nums[i] if add else -nums[i])

            return max(a,b)
        
        return dp(0, True)
