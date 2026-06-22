class Solution:
    def maxScore(self, A: List[int], B: List[int]) -> int:


        #pos, pos, neg, neg


        @cache
        def dp(i,j):

            if i == 4:
                return 0
            if j == len(B):
                return -1e12
            
            #if we don't choose this i
            a = dp(i, j+1)

            #if we do choose this number
            b = A[i]*B[j] + dp(i+1, j+1)

            return max(a,b)

        return dp(0,0)


