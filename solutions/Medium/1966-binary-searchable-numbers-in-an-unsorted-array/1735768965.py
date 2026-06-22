class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:


        n = len(nums)
        good = [True]*n
        high = -1e15
        for i in range(n):
            if high >= nums[i]:
                good[i] = False

            high = max(high, nums[i])
        low = 1e15
        for i in range(n-1, -1, -1):
            if low <= nums[i]:
                good[i] = False

            low = min(low, nums[i])

        return sum([1 if x else 0 for x in good])

        