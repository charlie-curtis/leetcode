class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:

        m,n = len(image), len(image[0])

        def col_contains(j):
            for i in range(m):
                if image[i][j] == "1":
                    return True
            return False

        def row_contains(i, lower_col, upper_col):
            for j in range(lower_col, upper_col+1):
                if image[i][j] == "1":
                    return True
            return False

        l = 0
        r = y

        #FTTTTTTTT
        while l <= r:
            mid = l + (r-l)//2
            if col_contains(mid):
                r = mid -1
            else:
                l = mid + 1

        lower_col = l

        l = y
        r = n-1

        #print(l,r, "l/r")

        #TTTTTTFFFF
        while l <= r:
            mid = l + (r-l)//2
            #print("mid is", mid)
            if col_contains(mid):
                #print("moving left")
                l = mid + 1
            else:
                #print("moving right")
                r = mid -1

        upper_col = r
        #print("UPPER COL", upper_col)


        l = 0
        r = x


        #FTTTTTTTT
        while l <= r:
            mid = l + (r-l)//2
            if row_contains(mid, lower_col, upper_col):
                r = mid -1
            else:
                l = mid + 1

        lower_row = l 

        l = x 
        r = m-1

        #TTTTTTFFFF
        while l <= r:
            mid = l + (r-l)//2
            if row_contains(mid, lower_col, upper_col):
                l = mid + 1
            else:
                r = mid -1

        upper_row = r


        a = upper_row - lower_row + 1
        b = upper_col - lower_col + 1

        #print(lower_col)
        #print(upper_col)

        #print(lower_row)
        #print(upper_row)

        return a*b