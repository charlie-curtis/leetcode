class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mn = ssum = 0
        ans = - 10**9

        for x in nums:
            ssum+=x
            ans = max(ans, ssum - mn)
            mn = min(mn, ssum)
        return ans
        