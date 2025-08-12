class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def range_sum(n):
            return n*(n+1)//2

        def check(v):
            to_left = index
            to_right = n-1-index

            a = range_sum(v-1) - range_sum(max(0,v-1-to_left))
            b = range_sum(v-1) - range_sum(max(0,v-1-to_right))

            #v = 3
            #y,x,x,x
            c=max(0, to_left-(v-1))
            d=max(0, to_right-(v-1))
            #2,1,0,0
            return v + a + b + c +d <= maxSum

        l = 1
        r = 10**9

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
        