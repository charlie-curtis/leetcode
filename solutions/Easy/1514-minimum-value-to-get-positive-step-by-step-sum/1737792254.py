class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        mmin = min(list(accumulate(nums, initial=0)))
        return abs(mmin)+1