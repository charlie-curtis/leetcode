class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        @cache
        def dp(i,used):
            if i == n:
                return 0

            a = dp(i+1, used)
            b = dp(i+1, used+1) + A[i]*(used+1)
            return max(a,b)
        return dp(0, 0)
        
        