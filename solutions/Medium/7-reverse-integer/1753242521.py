class Solution:
    def reverse(self, x: int) -> int:

        low = -2**31
        high = 2**31-1
        neg = x < 0
        if neg:
            x=-x

        cur = 0
        while x:
            lsb= x%10
            cut= (high + int(neg) -lsb)/10
            if cur > cut:
                return 0
            cur= cur*10 + x%10
            x//=10
        if neg:
            return -cur
        return cur