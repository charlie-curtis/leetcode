from sortedcontainers import SortedDict
class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:


        doubles = SortedDict()
        singles = SortedDict()

        ans = -1
        for i,x in enumerate(prices):

            #these 3 lines will try to find a compatible double (i,j) pair and make a triplet out of it
            idx = doubles.bisect_left(x)-1
            if idx != -1:
                ans = max(ans, profits[i] + doubles.peekitem(idx)[1])

            #try to extend doubles -- this will take the best single and see if it can make it into a double using i
            idx = singles.bisect_left(x)-1 #find a compatible price that is strictly less than x
            if idx != -1:
                score = singles.peekitem(idx)[1] + profits[i] 

                #find the price less than or equal to this price
                ins_idx = doubles.bisect_right(x)-1
                if ins_idx == -1 or doubles.peekitem(ins_idx)[1] < score:
                    #we are better, so insert
                    doubles[x] = score
                prune_idx = doubles.bisect_right(x)
                while prune_idx != len(doubles) and doubles.peekitem(prune_idx)[1] <= score:
                    doubles.popitem(prune_idx)

            #try to extend singles
            idx = singles.bisect_right(x)-1
            score = profits[i]
            if idx == -1 or singles.peekitem(idx)[1] < score:
                singles[x] = score

            prune_idx = singles.bisect_right(x)
            while prune_idx != len(singles) and singles.peekitem(prune_idx)[1] <= score:
                singles.popitem(prune_idx)


        return ans

            
