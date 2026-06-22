class Solution:
    def minOperations(self, nums: List[int]) -> int:
        A = [c for (c,g) in groupby(nums)]
        n = len(A)

        if A[0] == 1:
            return n-1
        return n