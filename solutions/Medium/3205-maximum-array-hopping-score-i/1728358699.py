class Solution:
    def maxScore(self, nums: List[int]) -> int:


        high = -1
        ans = 0
        for i in range(len(nums)-1, 0, -1):
            high = max(high, nums[i])
            ans+=high
        return ans
