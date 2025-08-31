class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        diags = [[set() for _ in range(3)] for _ in range(3)]

        n,m = len(board), len(board[0])

        def mark(i, j, x):
            rows[i].add(x)
            cols[j].add(x)
            diags[i//3][j//3].add(x)
        def unmark(i,j,x):
            rows[i].remove(x)
            cols[j].remove(x)
            diags[i//3][j//3].remove(x)

        
        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    mark(i,j, board[i][j])

        def backtrack(board, i,j):
            if j == m:
                return backtrack(board, i+1, 0)
            
            if i == n:
                return True

            if board[i][j] != '.':
                return backtrack(board, i, j+1)

            
            for x in range(1,10):
                x = str(x)
                if x in rows[i] or x in cols[j]:
                    continue
                if x in diags[i//3][j//3]:
                    continue
                
                board[i][j] = x
                mark(i,j, board[i][j])
                res = backtrack(board, i, j+1)
                if res:
                    return res
                unmark(i,j, board[i][j])
                board[i][j] = '.'

            return False
        
        backtrack(board, 0,0)

            

        