gcd_table = [[0 for _ in range(13)] for _ in range(13)]

for i in range(1,13):
    for j in range(1,13):
        gcd_table[i][j] = math.gcd(i,j)
class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:


        def get_valid(used):
            available = []
            for i in range(n):
                if used&(1<<i) == 0:
                    available.append(i)
            
            cnt = n - len(available)
            cur = cnt+1
            return [x for x in available if gcd_table[cur][x+1] == 1]


        def mark_used(used, x):
            return used|(1<<x)

        @cache
        def bt(used, i):

            if i == n:
                return 1

            options = get_valid(used)
            if len(options) == 0:
                return 0

            ans = 0
            for x in options:
                tmp = mark_used(used, x)
                ans+=bt(tmp, i+1)
            return ans

        return bt(0, 0)


            
                




        