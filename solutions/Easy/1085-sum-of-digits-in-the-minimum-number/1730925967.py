class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        mmin = min(nums)

        ssum = 0
        while mmin > 0:
            ssum+= mmin % 10
            mmin//=10

        return 1 if ssum % 2 == 0 else 0
        