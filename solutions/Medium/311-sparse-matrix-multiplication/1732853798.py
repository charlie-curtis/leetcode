class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        #2x3 * 3x3 -> 2x3

        #row1 * col1,col2, col3
        #ro2 * col1,col2, col3

        m,n = len(mat1), len(mat1[0])
        o,p = len(mat2), len(mat2[0])


        #https://www.mathsisfun.com/algebra/matrix-multiplying.html <---- look at the picture
        d2 = defaultdict(list)

        for i in range(o):
            for j in range(p):
                if mat2[i][j] != 0:
                    d2[i].append(j)

        out = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat1[i][j] != 0:
                    for k in d2[j]:
                        v = mat1[i][j] * mat2[j][k]
                        out[i][k]+=v

        return out

        