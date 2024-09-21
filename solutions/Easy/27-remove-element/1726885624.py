class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        j, n = 0, len(nums)

        for i in range(n):
            if nums[i] != val:
                nums[j], nums[i] = nums[i], nums[j]
                j+=1
        return j
        