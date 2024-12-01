class Solution:
    def smallestNumber(self, n: int) -> int:

        def isgood(n):
            return (n+1)&n == 0

        while True:
            if isgood(n):
                return n
            n+=1
        