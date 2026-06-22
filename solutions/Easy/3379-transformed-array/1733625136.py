class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0]*n
        for i in range(n):
            shift = nums[i]
            res[i] = nums[((i+shift)+n)%n]
        return res
        