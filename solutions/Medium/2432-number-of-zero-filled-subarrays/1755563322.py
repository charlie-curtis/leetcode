class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        ans = 0
        for c, g in groupby(nums):
            if c != 0:
                continue
            n = len(list(g))
            ans+=n*(n+1)//2
        return ans
        