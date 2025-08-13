class Solution:
    def minOperations(self, grid: List[List[int]], D: int) -> int:

        A = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                A.append(grid[i][j])

        A.sort()
        if len(A) == 1:
            return 0
        n = len(A)

        for i in range(n-1):
            if (A[i+1] - A[i]) % D != 0:
                return -1
        
        after = sum(A)
        before = 0
        ans = 10**9
        for i,x in enumerate(A):
            after-=x
            bexpected = i*x
            aexpected = (n-1 - i)*x

            cost = (after - aexpected)//D + (bexpected-before)//D
            ans = min(ans, cost)
            before+=x
        return ans



        