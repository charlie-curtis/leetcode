class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        r = 2**31-1

        #mid <= target
        #TTTTTTFFFFFF
        #return r
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid <= x:
                l = mid + 1
            else:
                r = mid - 1
        return r
        