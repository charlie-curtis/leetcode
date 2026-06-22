class Solution:
    def maxWeight(self, weights: List[int], w1: int, w2: int) -> int:
        weights.sort(reverse=True)
        n=len(weights)
        @cache
        def dp(i,x,y):
            if i == n:
                return 0
            options=[]
            options.append(dp(i+1,x,y))
            if x+weights[i] <= w1:
                options.append(dp(i+1,x+weights[i],y) + weights[i])
            if (x!=y or w1!=w2) and (y+weights[i] <= w2):
                options.append(dp(i+1,x,y+ weights[i]) + weights[i])

            return max(options)
        r = dp(0,0,0)
        dp.cache_clear()
        return r