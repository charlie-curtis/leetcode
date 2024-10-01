class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        m,n = len(board), len(board[0])
        def search(i,j, offset, used):

            if offset == len(word):
                return True

            if i >= m or i < 0 or j < 0 or j>=n:
                return False

            if used[i][j]:
                return False
            
            if board[i][j] != word[offset]:
                return False

            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            
            used[i][j] = True
            for x,y in dirs:
                if search(i+x, j+y, offset+1, used):
                    return True
            used[i][j] = False
            return False

        used = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if search(i,j, 0, used):
                    return True
        return False

            