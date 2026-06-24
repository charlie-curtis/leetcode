class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        i = j = 0
        m,n = len(mat), len(mat[0])

        left = -1
        right = n
        top = - 1
        bottom = m

        out = []
        #[[1, 2, 3, 4]
        #[ 5, 6, 7, 8]
        #[ 9, 10,11,12]]
        while len(out) < m*n:
            while (j < right and len(out) < m*n):
                out.append(mat[i][j])
                j+=1
            j-=1
            i+=1
            top+=1
            while (i < bottom and len(out) < m*n):
                out.append(mat[i][j])
                i+=1
            i-=1
            j-=1
            right-=1
            while (j > left and len(out) < m*n):
                out.append(mat[i][j])
                j-=1
            j+=1
            i-=1
            bottom-=1
            while (i > top and len(out) < m*n):
                out.append(mat[i][j])
                i-=1
            left+=1
            i+=1
            j+=1
        return out



        # 1 2 3
        # 4 5 6
        # 7 8 9


        