class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:

        m,n = len(grid), len(grid[0])

        def canreach(bi,bj, pi, pj, endx, endy):
            q = deque()
            q.append([pi,pj])
            seen = set()
            while q:
                curi, curj = q.popleft()

                if (curi, curj) == (endx, endy):
                    return True
                dirs = [[-1,0], [1,0], [0,1], [0,-1]]
                nxt = [(curi+x, curj+y) for (x,y) in dirs]

                for ni,nj in nxt:
                    if ni < 0 or nj < 0 or ni == m or nj == n or grid[ni][nj] == '#' or (ni,nj) in seen or (ni,nj) == (bi,bj):
                        continue
                    seen.add((ni,nj))
                    q.append([ni,nj])
            return False

        start = end = box = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    start = [i,j]
                if grid[i][j] == 'B':
                    box = [i,j]
                if grid[i][j] == 'T':
                    end = [i,j]
                
        q = deque()
        q.append([box[0], box[1], start[0], start[1], 0])
        seen = set()
        while q:
            bi,bj,pi, pj, cost = q.popleft()

            if bi == end[0] and bj == end[1]:
                return cost
            
            dirs = [[-1,0, 1,0], [1,0, -1, 0], [0,1, 0, -1], [0,-1, 0, 1]]
            nxt = [(bi+x, bj+y, bi+a, bj+b) for (x,y, a, b) in dirs]

            for ni,nj,canx,cany in nxt:
                if ni < 0 or nj < 0 or ni == m or nj == n or grid[ni][nj] == '#' or (bi,bj,ni,nj) in seen:
                    continue
                if canreach(bi,bj,pi,pj, canx, cany):
                    q.append([ni,nj,bi,bj, cost+1])
                    seen.add((bi,bj,ni,nj))
            
        return -1