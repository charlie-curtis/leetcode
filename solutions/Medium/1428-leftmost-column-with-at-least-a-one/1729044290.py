# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, bm: 'BinaryMatrix') -> int:

        m,n = bm.dimensions()

        def search(i):

            #FFFTTTTTTT
            l = 0
            r = n-1
            while l<=r:
                mid = l + (r-l)//2
                if bm.get(i, mid) == 1:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        ans = n
        for i in range(m):
            ans = min(ans, search(i))
        return ans if ans != n else -1
        