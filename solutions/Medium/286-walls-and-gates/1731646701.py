class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """


        m, n = len(rooms), len(rooms[0])
        grid = rooms

        q = deque()

        INF = 2147483647
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.appendleft([i,j, 0])



        dirs = [[-1, 0], [1,0], [0,-1], [0,1]]
        while q:
            i,j,dst = q.pop()
            
            if grid[i][j] != 0 and grid[i][j] != INF:
                continue
            
            grid[i][j] = min(dst, grid[i][j])
            for x,y in dirs:
                if i+x < 0 or j+y < 0 or i+x == m or j+y == n or grid[i+x][j+y] != INF:
                    continue
                q.appendleft([i+x, j+y, dst+1])

        