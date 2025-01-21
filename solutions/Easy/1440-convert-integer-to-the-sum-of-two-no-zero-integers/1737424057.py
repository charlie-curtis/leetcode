class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def good(x):
            while x > 0:
                if x % 10 == 0:
                    return False
                x//=10
            return True

        for i in range(1,n):
            a = i
            b = n-i
            if good(a) and good(b):
                return [a,b]
        