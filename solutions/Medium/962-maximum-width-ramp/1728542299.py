from sortedcontainers import SortedDict
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        stack = []
        n = len(nums)
        bests = [0]*n

        high = 0
        for i in range(n-1, -1, -1):
            high = max(nums[i], high)
            bests[i] = high

        j = 0
        ans = 0
        for i in range(n):
            while j < n and bests[j] >= nums[i]:
                j+=1
            ans = max(ans, j-i-1)
        return ans
        