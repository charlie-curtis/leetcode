class Solution:
    def maxScore(self, prices: List[int]) -> int:

        #when given an equation, we can rearrange it.
        #any numbers that satisfy price[i] - i = price[j] - j are pairable


        d = defaultdict(int)
        for i,x in enumerate(prices):
            d[i+1-x]+=x

        return max(d.values())
        