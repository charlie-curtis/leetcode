class Solution:
    def minCost(self, n: int) -> int:


        #100
        #99,1 -> 98,1 99*100/2 = 4950
        #10*10 = 100
        #5*5 = 25 + 25
        #3*2 = 6 + 6 

        @cache
        def dp(x):
            if x == 1:
                return 0
            
            if x % 2 == 0:
                a = b = x//2
            else:
                a = (x-1)//2
                b = (x+1)//2
            return a*b + dp(a) + dp(b)

        return dp(n)
        