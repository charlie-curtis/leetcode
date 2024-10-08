class Solution:
    def maxScore(self, nums: List[int]) -> int:


        high = -1
        n = len(nums)
        ans = 0
        for i in range(n-1, 0, -1):
            x = nums[i]
            high = max(high, x)
            ans+=high

        return ans
        