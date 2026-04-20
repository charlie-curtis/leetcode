class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        A = colors
        def compute(A):
            x = A[0]
            n = len(A)
            for i in range(n-1, 0, -1):
                if A[i] != x:
                    return i

        return max(compute(A), compute(A[::-1]))


        