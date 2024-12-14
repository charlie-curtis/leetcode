class Solution:
    def findShortestWay(self, maze: List[List[int]], start: List[int], destination: List[int]) -> str:

        #bfs, but search in this direction: D, L, R U
        dirs = [[1,0], [0,-1], [0,1], [-1,0]]
        q = deque()
        def is_wall(i,j):
            return i < 0 or j < 0 or i == m or j == n or maze[i][j] == 1
        m,n = len(maze), len(maze[0])

        
        for i in range(4):
            x,y = dirs[i]
            if not is_wall(x+start[0], y + start[1]):
                q.append((start[0], start[1], i, str(i)))
        seen = set()
        def convert(ins):
            A = ['d', 'l', 'r', 'u']
            return ''.join([A[int(x)] for x in ins])

        while q:
            x,y, dir, ins = q.popleft()
            ke = (x,y,dir)
            if is_wall(x,y):
                continue
            if ke in seen:
                continue
            seen.add(ke)

            nxt_x, nxt_y = dirs[dir][0] + x, dirs[dir][1]+ y

            if [x,y] == destination:
                return convert(ins)

            if is_wall(nxt_x, nxt_y):
                for i in range(4):
                    a,b = dirs[i]
                    q.append([x+a,y+b, i, ins + str(i)])
            else:
                q.append([nxt_x, nxt_y, dir, ins])
        return "impossible"