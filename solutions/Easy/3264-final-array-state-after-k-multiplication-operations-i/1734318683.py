class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for _ in range(k):
            mmin = min(nums)
            for i,x in enumerate(nums):
                if x == mmin:
                    nums[i] = x*multiplier
                    break
        return nums
        