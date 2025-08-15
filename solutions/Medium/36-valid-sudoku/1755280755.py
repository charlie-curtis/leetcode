class Solution:
    def isValidSudoku(self, g: List[List[str]]) -> bool:
        rows=defaultdict(Counter)
        cols=defaultdict(Counter)
        boxes=defaultdict(Counter)
        for i in range(9):
            for j in range(9):
                if g[i][j] == ".":
                    continue
                v = g[i][j]
                rows[i][v]+=1
                cols[j][v]+=1
                x=i//3*3+ j//3
                boxes[x][v]+=1

                if rows[i][v] > 1 or cols[j][v] > 1 or boxes[x][v] > 1:
                    return False
        return True