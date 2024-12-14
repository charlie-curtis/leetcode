class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], dest: List[int]) -> bool:


        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        seen = set()
        m,n = len(maze), len(maze[0])

        def is_wall(i,j):
            return i < 0 or j < 0 or i == m or j == n or maze[i][j] == 1

        def dfs(i,j, dir):

            ke = (i,j, dir)
            if is_wall(i,j):
                return False
            if ke in seen:
                return False

            seen.add(ke)
            
            x,y = i+dirs[dir][0], j + dirs[dir][1]


            if [i,j] == dest and is_wall(x,y):
                return True

            if is_wall(x,y):
                for k in range(len(dirs)):
                    a,b = dirs[k]
                    res = dfs(i+a, j+b, k)
                    if res:
                        return True
                return False
            else:
                return dfs(x,y, dir)


        return any([dfs(start[0],start[1],i) for i in range(4)])