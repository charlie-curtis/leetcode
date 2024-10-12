from sortedcontainers import SortedList
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:


        #bisect_left-1 will give me the element less than x
        #bisect_right will give me the elemtn > x

        def check(sl, x, k):

            idx = sl.bisect_left(x)-1
            if idx != -1 and x - sl[idx] == k+1:
                return True
            idx = sl.bisect_right(x)
            return idx != len(sl) and sl[idx] - x == k+1

        sl = SortedList()

        for i,x in enumerate(bulbs):
            sl.add(x)

            if check(sl, x, k):
                return i+1
        return -1


        