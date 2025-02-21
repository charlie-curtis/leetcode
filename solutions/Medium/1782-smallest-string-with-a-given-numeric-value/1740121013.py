class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        out = []
        while n > 0:
            rem = n-1
            other = k-26*rem
            chosen = max(other, 1)
            out.append(chr(ord('a')+chosen-1))
            k-=chosen
            n-=1
        return ''.join(out)
        