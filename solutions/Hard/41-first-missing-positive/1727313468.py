class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):

            while 1 <= nums[i] <= len(nums) and (nums[i] != nums[nums[i]-1]):
                j = nums[i] -1
                nums[j], nums[i] = nums[i], nums[j]

        for i,x in enumerate(nums):
            if i+1 != x:
                return i+1
        return len(nums)+1