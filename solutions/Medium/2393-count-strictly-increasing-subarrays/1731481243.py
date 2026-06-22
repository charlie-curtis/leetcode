class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        streak = 0
        prev = -1
        ans = 0
        for x in nums:
            if x > prev:
                streak+=1
            else:
                streak = 1
            prev = x
            ans+=streak
        return ans
        