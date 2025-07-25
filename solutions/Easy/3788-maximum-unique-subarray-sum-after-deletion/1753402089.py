class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        n = len(nums)

        A = [x for x in nums if x > 0]
        return sum(list(set(A)))