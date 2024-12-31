sys.setrecursionlimit(10**7)
class Solution:
    def findDerangement(self, n: int) -> int:

        #editorial

        #this problem was difficult and i relied on the editorial

        #assume you originally have some permutation [1,2,3,4,5] and are processing the i-th index
        #the cases are

        #A. put i in the j-th position. Assume j goes in the i-th position. In this case, both i and j are satisfied, and you can recurse for i-2 elements. You can make this decision i-1 times. This is where (i-1)*dp(i-2)
        #B. move i into the j-th position, BUT the j-th element does NOT go into the i-th position. That leaves a derangement of i-1, and you can make that move i-1 times. That is where (i-1)*dp(i-1) comes from. This case is brilliant

        M = 10**9 + 7
        @cache
        def dp(i):
            if i == 0:
                return 1
            if i == 1:
                return 0

            a = dp(i-2) %M
            b = dp(i-1) % M
            a*=(i-1)
            a%=M
            b*=(i-1)
            b%=M

            return (a + b)% M
        
        return dp(n)