from sortedcontainers import SortedDict
class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:

        singles = SortedDict()
        doubles = SortedDict()

        n = len(prices)
        ans = -1 
        for i in range(n):
            price = prices[i]
            profit = profits[i]

            #check for any triples we can make
            idx = doubles.bisect_left(price) -1
            if idx != -1:
                ans = max(ans, doubles.peekitem(idx)[1] + profit)

            #idx is a compatible single, so let's make a double
            idx = singles.bisect_left(price) -1
            if idx != -1:
                item = singles.peekitem(idx)
                can_total = profit + item[1]

                #prune
                while (idx := doubles.bisect_left(price)) != len(doubles):
                    if doubles.peekitem(idx)[1] > can_total:
                        break
                    doubles.popitem(idx)

                idx = doubles.bisect_right(price)-1
                if idx == -1 or doubles.peekitem(idx)[1] <= can_total:
                    doubles[price] = can_total

            while (idx := singles.bisect_left(price)) != len(singles):
                if singles.peekitem(idx)[1] > profit:
                    break
                singles.popitem(idx)

            #get the element that is just smaller than or equal to and see if we should insert
            idx = singles.bisect_right(price)-1
            if idx == -1 or singles.peekitem(idx)[1] < profit:
                singles[price] = profit
        return ans