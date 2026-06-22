class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:

        n = len(nums)
        #flag = True means we're first element
        @cache
        def dp(i, flag):
            if i == n:
                return 0

            a = dp(i+1, 1-flag) + (nums[i] if flag else -nums[i])
            b = dp(i+1, 0) + nums[i]
            return max(a,b)

        return dp(0, True)

        

        