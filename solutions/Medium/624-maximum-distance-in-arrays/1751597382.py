class Solution:
    def maxDistance(self, A: List[List[int]]) -> int:

        ans = 0
        n = len(A)

        zMin, zMax = A[0][0], A[0][-1]
        for i in range(1,n):
            ans = max(ans, A[i][-1] - zMin)
            ans = max(ans, zMax - A[i][0])

            zMax = max(zMax, A[i][-1])
            zMin = min(zMin, A[i][0])
        return ans