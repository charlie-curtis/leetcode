class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:


        cur = nums[-1] 
        ans = cur 
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] <= cur:
                cur+=nums[i]
            else:
                cur = nums[i]
            ans = max(ans, cur)
        return ans

        