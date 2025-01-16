class Solution:
    def xorAllNums(self, A: List[int], B: List[int]) -> int:
        m,n = len(A), len(B)

        ans = 0
        if n % 2 == 1:
            for i in range(m):
                ans^=A[i]

        if m % 2 == 1:
            for i in range(n):
                ans^=B[i]
        return ans

        