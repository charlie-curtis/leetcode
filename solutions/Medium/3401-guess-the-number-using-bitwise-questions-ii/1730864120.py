# Definition of commonBits API.
# def commonBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:

        ans = 0
        for i in range(32):
            before = commonBits(0)
            after = commonBits(1<<i)
            if after-before > 0:
                ans+=(1<<i)
        return ans
        