class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        m = len(board)
        d = {}
        for i in range(m):
            n = len(board[i])
            for j in range(n):
                d[board[i][j]] = [i,j]

        
        
        cur = [0,0]
        out = ""
        for s in target:
            newpos = d[s]

            x = cur[1] - newpos[1]
            y = cur[0] - newpos[0]
            goupfirst = cur == [5,0]

            if not goupfirst:
                if x > 0:
                    out+='L'*abs(x)
                elif x < 0:
                    out+='R'*abs(x)
                if y < 0:
                    out+='D'*abs(y)
                elif y > 0:
                    out+='U'*abs(y)
            else:
                if y < 0:
                    out+='D'*abs(y)
                elif y > 0:
                    out+='U'*abs(y)
                if x > 0:
                    out+='L'*abs(x)
                elif x < 0:
                    out+='R'*abs(x)
            out+='!'
            cur = newpos
        return out
            



        