class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        T = s.count('1')
        ans = T

        A = [[c, len(list(g))] for c,g in groupby(s)]

        n = len(A)
        for i in range(1, n-1):
            if A[i][0] != '1':
                continue
            ans = max(ans, T + A[i-1][1] + A[i+1][1])
        return ans


        