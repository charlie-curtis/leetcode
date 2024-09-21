class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return n

        d = [1,2]
        i = 2
        while i < n:
            d[-1], d[-2] = d[-1] + d[-2], d[-1]
            i+=1
        return d[-1]


        