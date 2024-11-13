from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:



        sl = SortedList()
        ans = 0
        for x in nums:

            l = sl.bisect_left(lower-x)-1
            r = sl.bisect_right(upper-x)-1
            ans+=r-l

            sl.add(x)
        return ans
        