class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        
        for x in [5,3,2]:
            while n % x == 0:
                n//=x
        return n == 1