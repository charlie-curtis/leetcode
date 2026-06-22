class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        have=reduce(xor,nums)
        return (have^k).bit_count()