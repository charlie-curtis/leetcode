class Solution:
    def maxOperations(self, A: List[int]) -> int:

        a = sum(A[:2])
        b = sum(A[-2:])
        c = A[0] + A[-1]

        @cache
        def dp(i,j, lookingFor):

            if i >= j:
                return 0
            
            a = b = c = 0
            if A[i] + A[j] == lookingFor:
                a = 1 + dp(i+1, j-1, lookingFor)
            if A[i] + A[i+1] == lookingFor:
                b = 1 + dp(i+2, j, lookingFor)
            if A[j] + A[j-1] == lookingFor:
                c = 1 + dp(i, j-2, lookingFor)

            return max([a,b,c])

        return max([dp(0, len(A)-1, x) for x in [a,b,c]])



        