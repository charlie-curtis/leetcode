class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:

        a,b,c = sorted([a,b,c])
        if a + b >= c:
            #no bottle neck
            return (a+b+c)//2
        #bottleneck on a+b
        return (a+b)