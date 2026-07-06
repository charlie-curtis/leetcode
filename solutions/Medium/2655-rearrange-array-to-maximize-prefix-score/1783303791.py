class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum([1 if x > 0 else 0 for x in list(accumulate(nums))])