class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:

        n = len(nums)
        total = sum(nums)
        pref = 0
        rem = total

        ans = -1e10 
        for x in nums:
            pref+=x
            ans = max(ans, pref, rem)
            rem-=x

        return ans
        