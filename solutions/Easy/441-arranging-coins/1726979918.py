class Solution:
    def arrangeCoins(self, n: int) -> int:

        #n = a(a+1)//2

        l = 0
        r = 2**30

        #TTTTTTTTFFFFFF
        #right
        while l <= r:
            mid = l + (r-l)//2
            if mid*(mid+1)//2 <= n:
                l = mid +1
            else:
                r = mid -1
        return r
