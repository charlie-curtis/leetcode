class Solution:
    def minDays(self, n: int) -> int:

        @cache
        def dp(x):
            #print(x)
            if x == 0:
                return 0
            if x == 1:
                return 1

            #eat enough to make it div by 2
            options = []
            options.append(x)


            t = x
            while t > 0 and t % 3 != 0:
                t-=1
            options.append(x-t+1 + dp(t//3))

            t = x
            while t > 0 and t % 2 != 0:
                t-=1
            options.append(x-t+1 + dp(t//2))
            
            return min(options)


        return dp(n)

        #10 -> 5 -> 4- > 2 -> 1 -> 0
        #10 -> 9 -> 6 -> 3 -> 1 -> 0