class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:


        cut = len(slices)//3

        def solve(A):
            n = len(A)
            @cache
            def dp(i, k):
                if i >= n or cut == k:
                    return 0
                a = dp(i+2, k+1) + A[i]
                b = dp(i+1, k)


                return max(a,b)
            
            res = dp(0,0)
            dp.cache_clear()
            return res


        
        a = solve(slices[:-1])
        b = solve(slices[1:])

        return max(a,b)
        