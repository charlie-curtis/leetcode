class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #want to bring a bigger value forward
        #[3,1,2] -> bring the 2 forward

        n = len(nums)
        pivot = -1
        swap_idx = -1
        for i in range(n):
            if i+1 < n and nums[i] < nums[i+1]:
                pivot = i
                swap_idx = i+1
            if pivot != -1 and nums[i] > nums[pivot]:
                if nums[i] < nums[swap_idx]:
                    swap_idx = i
        
        nums[pivot], nums[swap_idx] = nums[swap_idx], nums[pivot]
        nums[pivot+1:] = sorted(nums[pivot+1:])

        