#No SHOT I could solve this problem again. I used the editorial for the prefix sum precomputation, but I figured out pieces on my own, too

#This problem is basically trying to find the volume of a cube. So if you take the x-y plane as (j or k), then you can multiply each x,y coordinate by i
#which is how we got i*(i-1)//2 (we are subtracting 1 from the normal sum because we are indexed from 0 to n-1 -- instead of 1 to N)

#The precomputation part is figuring out the sum of a square (which in itself is a different leetcode problem using prefix sums on immutable arrays)
class Solution:

    pre = [[0 for _ in range(1300)] for _ in range(1300)]

    #precompute the sum of (j or k) for 0...1299
    #so if n = 1200, we can find the answer in constant time
    for i in range(1300):
        for j in range(1300):
            a = i|j
            pre[i][j] = a
            if i-1 >= 0:
                pre[i][j] +=pre[i-1][j]
            if j-1 >= 0:
                pre[i][j] +=pre[i][j-1]
            if i-1 >= 0 and j-1>=0:
                pre[i][j]-=pre[i-1][j-1]
    
    #this is basically a cube, so we want to compute the volume of a cube
    def maxSizedArray(self, s: int) -> int:

        def check(n):
            ssum = Solution.pre[n-1][n-1]

            return ssum*(n*(n-1))//2 <= s

        l = 0
        r = 1299
        #TTTFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1
        return r