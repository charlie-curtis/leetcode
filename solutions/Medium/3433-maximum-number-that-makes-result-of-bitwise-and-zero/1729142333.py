class Solution:
    def maxNumber(self, n: int) -> int:

        j = 0
        for i in range(64):
            if n&(1<<i) > 0:
                j = i

        return 2**j-1
        