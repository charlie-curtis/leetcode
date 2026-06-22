class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        n = len(nums)
        best = -1e15
        for i in range(n+1):
            best = max(best, abs(nums[i%n] - nums[(i+1)%n]))
        return best
        