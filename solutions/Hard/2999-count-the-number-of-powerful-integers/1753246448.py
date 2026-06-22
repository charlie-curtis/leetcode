class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suff: str) -> int:

        start, finish = str(start), str(finish)
        n1,n2 = len(finish), len(start)
        start = '0'*(n1-n2) + start #pad

        n = len(finish)
        m = len(suff)


        @cache
        def dp(i, tight_low, tight_high):
            if i == n:
                return 1
            
            s = int(start[i]) if tight_low else 0
            e = int(finish[i]) if tight_high else 9
            e = min(limit, e)

            #now handle limit
            rem = n-i
            if rem <= m:
                #need to use suffix
                s1 = int(suff[-rem])
                e2 = int(suff[-rem])
                if s1 < s or e2 > e:
                    return 0
                s = s1
                e = e2

            ans = 0
            for j in range(s,e+1):
                ans+=dp(i+1, tight_low & (j == int(start[i])), tight_high & (j == int(finish[i])))
            return ans

        return dp(0, True, True)
