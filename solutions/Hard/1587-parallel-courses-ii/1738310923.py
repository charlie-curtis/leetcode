class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:

        d = defaultdict(set)
        for u,v in relations:
            u-=1
            v-=1
            d[v].add(u)

        @cache
        def dp(x, locked, rem):
            if rem < 0:
                return 1e15
            if x == (2**n)-1:
                return 1

            ans = 1e15
            for i in range(n):
                if x&(1<<i) == 0:
                    good = True
                    for req in d[i]:
                        if x&(1<<req) == 0 or locked&(1<<req) > 0:
                            good = False
                            break
                    if good:
                        ans = min(ans, dp(x|(1<<i), locked|(1<<i), rem-1))

            if ans == 1e15:
                return dp(x,0,k) + 1
            return ans

        return dp(0,0, k)
                        
                            
                    

            