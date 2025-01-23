class Solution:
    def getKth(self, low: int, high: int, k: int) -> int:

        @cache
        def dp(v):
            if v == 1:
                return 0

            if v % 2 == 1:
                return 1 + dp(v*3+1)
            else:
                return  1 + dp(v//2)


        A = [[dp(x), x] for x in range(low, high+1)]
        A.sort()

        return A[k-1][1]
        