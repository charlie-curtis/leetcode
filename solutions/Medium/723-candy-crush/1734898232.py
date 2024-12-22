class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:


        m,n = len(board), len(board[0])
        while True:

            for x in board:
                print(*x)
            print()

            marked = set()
            for i in range(m):
                for j in range(n):
                    if j + 2 < n and board[i][j] == board[i][j+1] == board[i][j+2] and board[i][j] != 0:
                        marked.add((i,j))
                        marked.add((i,j+1))
                        marked.add((i,j+2))
                    if i + 2 < m and board[i][j] == board[i+1][j] == board[i+2][j] and board[i][j] != 0:
                        marked.add((i,j))
                        marked.add((i+1,j))
                        marked.add((i+2,j))

                
            if len(marked) == 0:
                break
            
            for j in range(n):
                p = m-1
                for i in range(m-1, -1, -1):
                    t = board[i][j]
                    board[i][j] = 0
                    if (i,j) not in marked:
                        board[p][j] = t
                        p-=1
        return board

            

                



        