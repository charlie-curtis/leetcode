class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #L, H, L, H
        #9, 11, 10,9
        n = len(nums)
        for i in range(1,n):
            wants_low = i % 2 == 0
            if wants_low and nums[i] > nums[i-1]:
                nums[i-1],nums[i] = nums[i], nums[i-1]
            elif not wants_low and nums[i] < nums[i-1]:
                nums[i-1],nums[i] = nums[i], nums[i-1]
            
