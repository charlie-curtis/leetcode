class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:


        l = 1
        r = 10**6
        m,n = len(grid),len(grid[0])
        target = m*n//2



        #true if more or exactly half of the elements are less than X
        def count(mid):

            left = 0
            right = 0
            for li in grid:
                left+=bisect_left(li, mid)
                right+=n-bisect_right(li,mid)
            
            return [left, right]
            
            


        
        #FFFFFFFFFTTTTTTT
        while l <= r:
            mid = l + (r-l)//2

            lc, rc = count(mid)

            if abs(lc - rc) <= m*n - lc - rc:
                #this handles the case where the median is duplicated abunch of times.
                #m*n -lc -rc is the unaccounted elements that EQUAL the midpoint that we're searching.
                #It basically means that we can add the unaccounted for elements to either side and make them equal
                return mid
            
            if lc > rc:
                r = mid - 1
            else:
                l = mid + 1


        return l

        


        