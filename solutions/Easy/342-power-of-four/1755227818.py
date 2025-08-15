good = set()

i = 1
while i <= 2**31 -1:
    good.add(i)
    i*=4
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        return n in good