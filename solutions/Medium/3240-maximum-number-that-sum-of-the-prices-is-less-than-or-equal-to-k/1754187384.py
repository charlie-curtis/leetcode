class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        l = 0
        r = 10**18

        @cache
        def dp(s, i, tight):
            n = len(s)
            if i == n:
                return [1,0]
            
            cutoff = int(s[i]) if tight else 1
            paths = special = 0
            for j in range(cutoff+1):
                res = dp(s, i+1, tight and j == int(s[i]))
                prev_paths, prev_special = res
                paths+=prev_paths
                special+=prev_special
                bit = n-i
                if j == 1 and (bit % x == 0):
                    special+=prev_paths
            return [paths,special]

        def check(mid):
            b = bin(mid)[2:]
            paths, special = dp(b, 0, True)
            dp.cache_clear()
            return special <= k


        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r