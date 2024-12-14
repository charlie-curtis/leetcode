class Solution:
    def newInteger(self, n: int) -> int:

        #This is NOT how you do this problem

        def get_msb_and_multi(x):
            msb = -1
            multi = 1
            while x > 0:
                msb = x % 10
                x//=10
                multi*=10
            return [msb, multi//10]

        #dp(x) = how many positive numbers <= x don't have 9 in them?

        @cache
        def dp(x):
            if x <= 8:
                return x

            ans = 0

            msb, multi = get_msb_and_multi(x)

            if x == multi:
                return 1 + dp(multi-1)
            
            if msb == 9:
                ans+=8*dp(multi)
            else:
                ans+=msb*dp(multi)

            ans+=dp(x-multi*msb)
            return ans
            
            #381
            #dp(381)
            #i'm processing 3, so 3*dp(100)
            # + dp(81)

            #231
            #20-3

            #dp(81) =  8*dp(10) + dp(1)
            #what if its 931
            #8*dp(100) + dp(31)

        l = 0
        r = 10**15

        #TTTTTTTFFFFf
        while l <= r:
            mid = l + (r-l)//2
            #dp.cache_clear()
            if dp(mid) <= n:
                l = mid + 1
            else:
                r = mid - 1
        

        test = str(r)
        out = ""
        for x in test:
            if x == '9':
                x = '8'
            out+=x

        return int(''.join(out)) 

