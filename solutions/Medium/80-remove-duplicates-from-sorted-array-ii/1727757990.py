class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)
        cur = 2
        n = len(nums)
        for i in range(2,n):
            if (nums[i] != nums[cur-1]) or (nums[i] != nums[cur-2]):
                nums[cur] = nums[i]
                cur+=1

        return cur
        