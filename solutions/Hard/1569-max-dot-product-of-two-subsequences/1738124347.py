class Solution:
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:

        m,n = len(A), len(B)
        @cache
        def dp(i,j):
            if i == m or j == n:
                return -1e15 

            a = A[i]*B[j] + dp(i+1, j+1)
            b = A[i]*B[j]
            c = dp(i+1,j)
            d = dp(i, j+1)

            return max(a,b,c, d)
        return dp(0,0)
        