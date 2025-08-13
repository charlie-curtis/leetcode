class Solution:
    def minOperations(self, grid: List[List[int]], D: int) -> int:

        A = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                A.append(grid[i][j])

        n = len(A)

        if n == 1:
            return 0
        A.sort()
        med = A[n//2]

        cost = 0
        for i in range(n):
            x = int(abs(A[i] - med))
            if x % D:
                return -1
            cost+=x//D
        return cost