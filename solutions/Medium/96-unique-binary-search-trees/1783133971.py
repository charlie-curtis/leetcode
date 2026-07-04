class Solution:
    def numTrees(self, n: int) -> int:

        #AC'd on my own, but further optimized using the editorial after
        #key observation is that we don't need to track the actual values in our range, just the size of the range
        @cache
        def fx(n):
            if n <= 1:
                return 1
            
            ans = 0
            for x in range(1,n+1):
                #x is the root
                a = fx(x-1)
                b = fx(n-x)
                ans+=a*b
            return ans

        return fx(n)