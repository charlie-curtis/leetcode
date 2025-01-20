class Solution:
    def canPartition(self, A: List[int]) -> bool:

        T = sum(A)
        if T % 2 == 1:
            return False
        
        n = len(A)
        @cache
        def dp(i, b):
            if i == n:
                return b == 0

            return dp(i+1, b-A[i]) or dp(i+1, b+A[i])
        return dp(0, 0)


        