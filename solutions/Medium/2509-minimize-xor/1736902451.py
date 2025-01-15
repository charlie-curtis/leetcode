class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        ans = 0
        bits = num2.bit_count()
        for i in range(32, -1, -1):
            if bits == 0:
                break
            isset = num1&(1<<i) > 0
            rem = i+1
            if isset or bits == rem:
                ans|=(1<<i)
                bits-=1
        return ans


