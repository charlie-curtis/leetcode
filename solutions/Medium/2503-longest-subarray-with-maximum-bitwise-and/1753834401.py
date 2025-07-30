class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        #i wrote this using sliding window before and counting individual bit positions. after looking at the editorial, there is a simpler way
        mx = max(nums)

        ans = 0
        for c, g in groupby(nums):
            if c == mx:
                ans = max(ans, len(list(g)))
        return ans

