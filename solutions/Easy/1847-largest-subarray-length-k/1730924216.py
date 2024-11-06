class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        best_start = max(nums[0:n-k+1])

        for i,x in enumerate(nums):
            if x == best_start:
                return nums[i:i+k]
        return -1
        