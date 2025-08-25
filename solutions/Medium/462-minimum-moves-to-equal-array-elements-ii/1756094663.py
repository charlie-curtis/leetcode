class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        m = int(median(nums))
        return sum([abs(x - m) for x in nums])
        