class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            t = 0
            while n:
                t+= (n%10)**2
                n//=10
            n = t
        return True



        