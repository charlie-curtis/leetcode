class Solution:
    def minCost(self, m: int, n: int) -> int:


        if m == n == 1:
            return 1
        if (m,n) in [(2,1), (1,2)]:
            return 3
        return -1