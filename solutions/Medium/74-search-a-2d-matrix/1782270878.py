class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:


        m,n = len(mat), len(mat[0])

        l = 0
        r = m-1

        #returns true if the first element in the row is <= target
        def check(row):
            return mat[row][0] <= target

        #TTTTTFFFF
        while (l <= r):
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        row = r
        l = 0
        r = n-1
        def check2(col):
            return mat[row][col] <= target
        while (l <= r):
            mid = l + (r-l)//2
            if check2(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        col = r
        return 0 <= row < m and 0 <= col < n and mat[row][col] == target


        