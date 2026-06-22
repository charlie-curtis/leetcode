class Solution:
    def maxCollectedFruits(self, g: List[List[int]]) -> int:

        #this is worded tricky, but you can solve each persons problem independently
        n = len(g)

        ans = sum([g[i][i] for i in range(n)])
        @cache
        def dp1(i,j,k):
            if i == n-1 and j == n-1:
                return 0
            if min(i,j) < 0 or max(i,j) == n or k == 0:
                return float('-inf')
            if i == j:
                return float('-inf')
            
            a = dp1(i+1,j+1, k-1)
            b = dp1(i-1, j+1, k-1)
            c = dp1(i, j+1, k-1)

            return max(a,b,c) + g[i][j]

        @cache
        def dp2(i,j,k):
            if i == n-1 and j == n-1:
                return 0
            if min(i,j) < 0 or max(i,j) == n or k == 0:
                return float('-inf')
            if i == j:
                return float('-inf')
            
            a = dp2(i+1,j-1, k-1)
            b = dp2(i+1, j,k-1)
            c = dp2(i+1, j+1,k-1)

            return max(a,b,c) + g[i][j]


        a = dp1(n-1, 0, n-1)
        b = dp2(0, n-1, n-1)
        c = ans

        print(a,b,c)
        return a + b + c