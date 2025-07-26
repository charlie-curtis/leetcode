class Solution:
    def trap(self, nums: List[int]) -> int:

        n = len(nums)
        to_left = [0]*n

        stack = []
        mx = 0
        for i in range(n):
            to_left[i] = mx
            mx = max(nums[i], mx)
        
        ans = 0
        mx = 0
        for i in range(n-1, -1, -1):
            ans+=max(0, min(to_left[i], mx) - nums[i])
            mx = max(nums[i], mx)
        return ans



        