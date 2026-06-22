class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:

        c1 = c2 = 0
        d = defaultdict(int)
        ans = 0
        d[0] = 1
        balance = 0
        for i,x in enumerate(s):
            balance+=num2 if x == '0' else -num1

            ans+=d[balance]
            d[balance]+=1

        return ans

        #num1 = 1, num2 = 2

        #1,2 (0,1)
        #2,4 (0,1)
        #num2, num1 num1 num2 num2 num1 num1

        #2, 1 0 2 4 3 2


        #5,5 = 1
        #1,2
        #1,2
        #7,8 = 7/8

        #10,10 = 0, 1
        #14,16 = 0, 1

        #

        #looking for 2/3 = .666
