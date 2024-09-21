class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[cur]:
                cur+=1
                nums[cur] = nums[i]
        return cur+1

        