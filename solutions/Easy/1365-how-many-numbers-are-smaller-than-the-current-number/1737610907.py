class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        A = sorted(nums)

        out = []
        for x in nums:
            out.append(bisect_left(A, x))
        return out
        