class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10**9+7
        @cache
        def fast(base, n):
            if n <= 0:
                return 1
            
            if n % 2 == 1:
                return base*fast(base, n-1) % MOD
            
            return fast(base, n//2) % MOD *fast(base, n//2) % MOD
        
        evens = n//2 + n%2
        odds = n//2

        a = fast(5, evens) % MOD
        b = fast(4, odds) % MOD
        return a*b % MOD
        

            


        