class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        #you can solve this problem via simulation, but trying to find the O(N) way

        '''
        [1+2,2+3, 3+4, 4+5]
        [1+2+2+3, 2+3+3+4, 3+4+4+5]
        [1+2+2+3+2+3+3+4, 2+3+3+4 + 3+4+4+5]
        [1+2+2+3+2+3+3+4 + 2+3+3+4+3+4+4+5]

        #1 appears once
        #2 appears n-1 times
        #3 appears 6 times
        #4 appears n-1 times
        #5 appears once

        #pascals triangle?


        The formula for a single row in pascals triangle is previous_val * (n-k+1)/1
        '''

        last = -1
        n = len(nums)-1
        ans = 0
        out = []
        for k,x in enumerate(nums):
            if k == 0 or k == len(nums)-1:
                last = 1
                ans+=x
                ans%=10
            else:
                #last*(n-k+1)/k
                last = last*(n-k+1)//k
                ans+=last*x
                ans%=10
            out.append(last)
                



        return ans
        
        