from sortedcontainers import SortedList
class Solution:
    def smallestRange(self, A: List[List[int]]) -> List[int]:

        n = len(A)
        ptrs = [1]*n
        sl = SortedList()
        for i,l in enumerate(A):
            sl.add([l[0], i])

        ans = 1e10 
        r = []
        while len(sl) == n:
            small,high = sl[0],sl[-1]
            can = high[0] - small[0]
            if can < ans:
                ans = can
                r = [small[0],high[0]]
            
            i = small[1]
            ptr = ptrs[i]
            del sl[0]
            if ptr < len(A[i]):
                sl.add([A[i][ptr], i])
                ptrs[i]+=1
        return r







        