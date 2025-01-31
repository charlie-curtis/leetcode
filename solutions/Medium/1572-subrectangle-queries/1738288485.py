class SubrectangleQueries:

    def __init__(self, R: List[List[int]]):
        self.A = R
        self.m = len(R)
        self.n = len(R[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.A[i][j] = newValue
        

    def getValue(self, row: int, col: int) -> int:
        return self.A[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)