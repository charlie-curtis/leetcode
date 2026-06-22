class Solution:
    def minimizedMaximum(self, n: int, quant: List[int]) -> int:



        #FFFFFFFFTTTTTTT

        m = len(quant)
        def check(mid):

            stores = 0
            for x in quant:
                stores+=(x+mid-1)//mid

            return stores <= n


        l = 1
        r = 10**5


        while l <= r:
            mid = l + (r-l)//2

            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l
        