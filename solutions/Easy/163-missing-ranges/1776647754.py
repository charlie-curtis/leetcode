class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = []
        n = len(nums)
        expected = lower
        for i in range(n):
            if nums[i] != expected:
                ans.append([expected, nums[i]-1])
            expected = nums[i] + 1
        if expected != upper+1:
            ans.append([expected, upper])
        return ans