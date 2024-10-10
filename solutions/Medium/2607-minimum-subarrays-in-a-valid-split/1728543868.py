class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:


        n = len(nums)

        def get_factors(x):

            i = 2
            out = set()
            while i*i <= x:
                while x % i == 0:
                    x//=i
                    out.add(i)
                i+=1
            if x != 1:
                out.add(x)

            return out

        
        factors = [get_factors(x) for x in nums]


        @cache
        def dp(i):

            if i == n:
                return 0

            best = 1e10
            for j in range(i,n):
                if len(factors[j]&factors[i]) > 0:
                    best = min(best, 1 + dp(j+1))
            return best

        ans = dp(0)
        return ans if ans < 1e10 else -1


        