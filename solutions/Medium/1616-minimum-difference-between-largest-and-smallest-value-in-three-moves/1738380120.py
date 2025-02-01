class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        print(nums)
        if len(nums) <= 4:
            return 0

        k = n-3
        best = 1e15
        for i in range(n-k+1):
            best = min(best, nums[i+k-1] - nums[i])
        return best