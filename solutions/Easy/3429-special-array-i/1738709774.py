class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        nums = [x % 2 for x in nums]
        return all([a != b for (a,b) in zip(nums, nums[1:])])