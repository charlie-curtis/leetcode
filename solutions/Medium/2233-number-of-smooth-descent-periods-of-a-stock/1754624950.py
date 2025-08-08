class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        ans = 0
        for _,g in groupby(enumerate(prices), key= lambda v: v[0] + v[1]):
            n = len(list(g))
            ans+=n*(n+1)//2
        return ans
        