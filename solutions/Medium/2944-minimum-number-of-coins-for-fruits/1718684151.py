class Solution:
    def minimumCoins(self, prices: List[int]) -> int:

        @cache
        def dp(i):
            #print(str(i) + "I")
            if i >= len(prices):
                return 0
            if i+1 == len(prices):
                #last
                return prices[i]

            cost = prices[i]
            can = float('inf') 
            free_moves = i+1
            for j in range(i+1, min(i+2+free_moves, len(prices)+1)):
                #print('searching' + str(j))
                can = min(can, dp(j))
                #print(can)

            #print(cost+can)
            return cost + can

        return dp(0)

