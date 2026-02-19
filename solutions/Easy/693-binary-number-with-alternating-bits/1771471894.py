class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        last = -1
        while n:
            bit = n % 2
            n//=2
            if bit == last:
                return False
            last = bit
        return True


        