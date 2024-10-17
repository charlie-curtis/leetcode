class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:

        n = len(nums)
        pos = [-1e10]*n
        neg = [-1e10]*n

        pos[0] = nums[0]
        for i in range(1,n):
            pos[i] = max(neg[i-1] + nums[i], nums[i])
            neg[i] = pos[i-1] - nums[i]

        return max(max(neg), max(pos))
        