class Solution:
    def confusingNumber(self, n: int) -> bool:

        d = {}
        d[9] = 6
        d[6] = 9
        d[0] = 0
        d[1] = 1
        d[8] = 8

        other = 0
        original = n
        while n > 0:
            x = n % 10
            if x not in d:
                return False
            other = other*10 + d[x]
            n//=10

        return other != original
        