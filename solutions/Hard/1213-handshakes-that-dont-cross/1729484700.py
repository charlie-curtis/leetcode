class Solution:
    def numberOfWays(self, n: int) -> int:


        MOD = 10**9 + 7
        @cache
        def dp(size):

            if size % 2 != 0:
                return 0
            if size == 0:
                return 1
            
            ans = 0
            #if size is 4, then we have numbers 1 to 4
            #then let's simulate connecting 1 to everything else
            #so 1 to 2, 1 to 3, 1 to 4
            for k in range(2,size+1):
                #1 gets connected to k
                i = 1
                left_size = k-1 - (i+1) + 1 #[i+1, k-1]
                right_size = size - (k+1) + 1  #[k+1, size]
                ans+= (dp(left_size) * dp(right_size))
                ans%=MOD
            return ans

        return dp(n) % MOD


