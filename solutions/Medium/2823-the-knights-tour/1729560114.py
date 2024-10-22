class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:

        pos = [[-1 for _ in range(n)] for _ in range(m)]

        def bt(r,c, cnt):

            pos[r][c] = cnt

            if n*m -1 == cnt:
                return True
            
            dirs = [[2,1], [-2,-1], [-2,1], [2,-1], [-1,-2], [1,2], [-1,2], [1,-2]]


            for x,y in dirs:
                x,y = r+x, y+c
                if x < 0 or x>=m:
                    continue
                if y < 0 or y>=n:
                    continue
                if pos[x][y] != -1:
                    continue
                res = bt(x,y, cnt+1)
                if res:
                    return True
            pos[r][c] = -1
            return False

        res = bt(r,c, 0)

        if not res:
            raise ValueError("Wrong")
        return pos


        