
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        d = defaultdict(int)
        for u,v,c in transactions:
            d[u]+=c
            d[v]-=c

        
        A = [v for k,v in d.items() if v != 0]
        
        n = len(A)

        #editorial. I didn't come close to solving initially, then i got AC after reading the editorial,
        #then i rewrote it to run faster based on the editorial's version

        #this problem basically reduces into "max number of sets we can take where the sum is 0"
        @cache
        def dp(state):

            if state == 0:
                return 0

            ssum = 0
            for i in range(n):
                if (1<<i)&state > 0:
                    ssum+=A[i]
            best = 0
            for i in range(n):
                if (1<<i)&state > 0:
                    best = max(best, dp(state^(1<<i)))

            #if the input sum = 0, then the group was balanced originally
            if ssum == 0:
                best+=1
            return best
        m = dp((1<<n)-1)
        return n-m
