class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        n= len(nums)
        best = nums[0] 
        cur = best
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                cur+=nums[i]
            else:
                cur = nums[i]
            
            best = max(best, cur)
        return best
        