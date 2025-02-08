class Solution:
    def getMaximumGenerated(self, n: int) -> int:


        d = defaultdict(int)
        d[0] = 0
        d[1] = 1

        for i in range(n+1):
            d[2*i] = d[i]
            d[2*i + 1] = d[i] + d[i+1]

        mmax = 0
        for i in range(n+1):
            mmax = max(d[i], mmax)
        return mmax


            
            
        