class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        pos = {}
        for i,x in enumerate(sorted(nums)):
            pos[x] = i

        for i,x in enumerate(nums):
            j = pos[x]
            for k in range(i, j+1):
                if nums[i].bit_count() != nums[k].bit_count():
                    return False
        return True


        