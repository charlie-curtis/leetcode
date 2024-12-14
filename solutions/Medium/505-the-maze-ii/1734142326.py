class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:


        dirs = [[0,-1], [0,1], [1,0], [-1,0]]
        q = deque([(start[0], start[1], i, 0) for i in range(4)])

        m,n = len(maze), len(maze[0])
        def is_wall(i,j):
            return i < 0 or j < 0 or i == m or j == n or maze[i][j] == 1
        
        seen = set()
        while q:

            x,y, dir, cost = q.popleft()
            ke = (x,y,dir)
            if is_wall(x,y):
                continue
            if ke in seen:
                continue
            seen.add(ke)

            nxt_x, nxt_y = dirs[dir][0] + x, dirs[dir][1]+ y

            if [x,y] == destination and is_wall(nxt_x, nxt_y):
                return cost

            if is_wall(nxt_x, nxt_y):
                for i in range(4):
                    q.appendleft([x,y, i, cost])
            else:
                q.append([nxt_x, nxt_y, dir, cost+1])
        return -1


        