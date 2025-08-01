class Solution:
    def trailingZeroes(self, n: int) -> int:

        #get the factors of the numbers. Count 2*5 pairs
        #there is a log way to do it (n//5 + n//25 + n//125...)
        dp2 = [0]*(n+1)
        dp5 = [0]*(n+1)
        for x in range(2,n+1):
            if x % 2 == 0:
                dp2[x] = 1 + dp2[x//2]
            if x % 5 == 0:
                dp5[x] = 1 + dp5[x//5]
        
        a = sum(dp2)
        b = sum(dp5)
        return min(a,b) # a > b, so we don't actually need dp[2]