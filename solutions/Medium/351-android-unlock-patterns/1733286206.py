class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        mapping = defaultdict(int)
        mapping[(1,3)] = 2
        mapping[(1,7)] = 4
        mapping[(1,9)] = 5
        mapping[(2,8)] = 5
        mapping[(3,1)] = 2
        mapping[(3,9)] = 6
        mapping[(3,7)] = 5
        mapping[(4,6)] = 5
        mapping[(6,4)] = 5
        mapping[(7,9)] = 8
        mapping[(7,1)] = 4
        mapping[(7,3)] = 5
        mapping[(8,2)] = 5
        mapping[(9,1)] = 5
        mapping[(9,3)] = 6
        mapping[(9,7)] = 8

        for t in mapping:
            a,b = t
            if mapping[(a,b)] != mapping[(b,a)]:
                print(a,b)
                raise ValueError("wrong")

        @cache
        def dp(cur, i, rem):
            if rem == 0:
                return 1

            ans = 0
            for j in range(1,10):
                if (1<<j)&cur:
                    #already used
                    continue
                #let's connect i to j
                if (i,j) in mapping:
                    req = mapping[(i,j)]
                    if (1<<req)&cur == 0:
                        #we are passing through a center that hasn't been used yet
                        continue
                ans+=dp(cur|(1<<j), j, rem-1)
            return ans

        
        return sum([dp(0,0,i) for i in range(m,n+1)])


        