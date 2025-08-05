class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        ans = 0
        for c,g in groupby(nums):
            if c == 1:
                ans = max(ans, len(list(g)))
        return ans
        