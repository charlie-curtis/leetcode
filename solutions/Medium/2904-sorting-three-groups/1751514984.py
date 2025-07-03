class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        n = len(nums)

        A = []
        for x in nums:
            if not A or A[-1] <= x:
                A.append(x)
            else:
                idx = bisect_right(A, x)
                A[idx] = x
        return n - len(A)

        