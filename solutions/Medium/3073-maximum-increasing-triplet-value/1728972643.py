from sortedcontainers import SortedDict
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        singles = SortedDict()
        doubles = SortedDict()

        ans = 0
        for x in nums:
            #look for a triple by searching the doubles
            #can only use numbers that i'm greater than
            idx = doubles.bisect_left(x)-1
            if idx != -1:
                ans = max(ans, x + doubles.peekitem(idx)[1])
            #look for the best double by searching singles
            idx = singles.bisect_left(x)-1
            if idx != -1:
                can = singles.peekitem(idx)[1] - x
                prev = doubles.bisect_right(x)-1
                if prev == -1 or can > doubles.peekitem(prev)[1]:
                    #we should insert
                    #but also we should prune any numbers that are obsoleted
                    idx = doubles.bisect_left(can)
                    while idx < len(doubles) and can >= doubles.peekitem(idx)[1]:
                        doubles.popitem(idx)
                    doubles[x] = can

            #add to single
            idx = singles.bisect_right(x)-1
            if idx == -1 or x > singles.peekitem(idx)[1]:
                #also remove any obsoleted numbers
                idx = singles.bisect_left(x)
                while idx < len(singles) and x >= singles.peekitem(idx)[1]:
                    singles.popitem(idx)
                singles[x] = x
        return ans
        