class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        out = [[-1 for i in range(n)] for _ in range(n)]

        left = top = 0
        right = bottom =  n-1
        cur = 1
        while cur < n*n+1:

            #left to right
            for j in range(left, right+1):
                out[top][j] = cur
                cur+=1

            for i in range(top+1, bottom+1):
                out[i][right] = cur
                cur+=1
            
            if top != bottom:
                for j in range(right-1, left-1, -1):
                    out[bottom][j] = cur
                    cur+=1
            if left != right:
                for i in range(bottom-1, top, -1):
                    out[i][left] = cur
                    cur+=1

            left+=1
            right-=1
            bottom-=1
            top+=1

        return out

