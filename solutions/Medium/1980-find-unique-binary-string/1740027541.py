class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        se = set(nums)
        n = len(nums[0])

        for x in range(2**n):
            b = bin(x)[2:]
            if len(b) < n:
                b = "0"*(n-len(b))+b
            if b not in se:
                return b
        return "-1"

        