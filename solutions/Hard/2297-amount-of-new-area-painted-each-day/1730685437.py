from sortedcontainers import SortedList
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        sl = SortedList()
        mmax = max([x[1] for x in paint])

        #this problem uses weird "PAINT BETWEEN" conditions where painting between 1-4 is considered 3 instead of 4,
        #so in order to model that better, i'm using .5 to represent the area between two numbers (i.e. 2.5 to represent between 2 and 3)
        for i in range(mmax):
            sl.add(i+ .5)

        out = []
        for start,end in paint:
            idx = sl.bisect_left(start)
            cnt = 0
            while idx < len(sl) and sl[idx] < end:
                cnt+=1
                del sl[idx]
            out.append(cnt)
        return out
        