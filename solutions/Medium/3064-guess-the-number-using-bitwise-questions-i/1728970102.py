# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        ans = 0
        for i in range(30):
            if commonSetBits(1<<i):
                ans^=1<<i

        return ans
            
        