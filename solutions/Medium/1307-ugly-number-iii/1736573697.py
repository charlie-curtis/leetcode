class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        #a+b+c -ab -ac -bc +abc

        #div by a = x//a
        #div by b = x//b
        #div by c = x//c

        def check(x):
            t = x//a + x//b + x//c
            ab = x//lcm(a,b)
            ac = x//lcm(a,c)
            bc = x//lcm(b,c)
            abc = x//lcm(a,b,c)

            res = t - ab - ac - bc + abc
            return res <= n

        

        l = 0
        r = 2*10**9


        #check(mid) -> return true if number of ugly numbers <= n

        #TTTTFFFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1
        
        #we normally return r here, but in this case, we don't want to return the largest r because it might
        #not actually be divisble by a,b, or c. Instead, we can going to find the smallest value <= r such that
        #check(r) == true

        options = []
        options.append(r//a*a)
        options.append(r//b*b)
        options.append(r//c*c)

        return max(options)
