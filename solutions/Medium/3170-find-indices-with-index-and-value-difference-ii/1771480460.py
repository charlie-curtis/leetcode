class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        if valueDifference == 0 and indexDifference == 0:
            return [0,0]

        mmin = 10**9
        mmax = -10**9
        minindex = maxindex = -1
        n = len(nums)

        for i in range(indexDifference,n):
            if nums[i-indexDifference] < mmin:
                mmin = nums[i-indexDifference]
                minindex = i-indexDifference
            if nums[i-indexDifference] > mmax:
                mmax = nums[i-indexDifference]
                maxindex = i-indexDifference

            if (nums[i] - mmin >= valueDifference):
                return [minindex, i]
            if (mmax - nums[i] >= valueDifference):
                return [maxindex, i]
        return [-1, -1]
            

        