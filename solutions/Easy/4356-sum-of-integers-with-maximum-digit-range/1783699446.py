class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:



        def getrange(x):
            digits = []
            while x:
                digits.append(x%10)
                x//=10
            digits.sort()

            return digits[-1] - digits[0]

        mmax = max(nums)

        ranges = [getrange(x) for x in nums]
        mmax = max(ranges)
        out = 0
        for i in range(len(nums)):
            if ranges[i] == mmax:
                out+=nums[i]
        return out