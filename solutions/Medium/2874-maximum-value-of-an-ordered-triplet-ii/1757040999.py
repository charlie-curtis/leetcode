class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        n = len(nums)
        mx = 0
        right = [0]*n
        for i in range(n-1, -1, -1):
            right[i] = mx
            mx = max(mx, nums[i])

        mx = ans = 0
        for i in range(n-1):
            ans = max(ans, (mx - nums[i]) * right[i])
            mx = max(nums[i], mx)
        return ans

        