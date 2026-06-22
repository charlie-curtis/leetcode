class Solution:
    def numberOfSets(self, n: int, k: int) -> int:


        #I struggled
        MOD = 10**9 + 7
        @cache
        def dp(x,isStart,k):
            if k < 0:
                return 0
            if x == n:
                return int(k == 0 and not isStart)

            #startPoint
            a = b = c = 0
            if isStart:
                a = dp(x, False, k-1)
                #we can assign this to the endpoint
            if not isStart:
                #we can assign this to the endpoint
                b = dp(x+1, True, k)
            
            c = dp(x+1, isStart, k)

            return (a+b+c) % MOD
            
        return dp(0,False,k)