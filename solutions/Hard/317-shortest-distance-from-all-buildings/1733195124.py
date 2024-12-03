class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones+=1


        zeros = m*n-ones

        INF = 10**9
        def searchFromZeros(a,b):

            seen = set()

            q = deque()
            q.append([a,b, 0])
            ans = 0
            found = 0
            dirs = [[-1,0], [1,0], [0,1], [0,-1]]

            while q:
                cur_x, cur_y, cost = q.popleft()
                nxt = [(cur_x + x, cur_y + y) for x,y in dirs]
                for i,j in nxt:
                    if i < 0 or i == m or j < 0 or j == n or (i,j) in seen or grid[i][j] == 2:
                        continue
                    seen.add((i,j))
                    if grid[i][j] == 1:
                        found+=1
                        ans+=cost+1
                    else:
                        q.append([i,j, cost+1])

            return ans if found == ones else INF

        def searchFromOnes(a,b, dst, C):
            seen = set()

            q = deque()
            q.append([a,b, 0])
            dirs = [[-1,0], [1,0], [0,1], [0,-1]]

            while q:
                cur_x, cur_y, cost = q.popleft()
                nxt = [(cur_x + x, cur_y + y) for x,y in dirs]
                for i,j in nxt:
                    if i < 0 or i == m or j < 0 or j == n or (i,j) in seen or grid[i][j] == 2:
                        continue
                    seen.add((i,j))
                    if grid[i][j] == 0:
                        C[(i,j)]+=1
                        dst[i][j]+=cost+1
                        q.append([i,j, cost+1])

        if zeros <= ones:
            best = INF
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        best = min(best, searchFromZeros(i,j))
    
            return best if best != INF else -1
        else:
            dst = [[0 for _ in range(n)] for _ in range(m)]
            C = Counter()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        searchFromOnes(i,j, dst, C)

            best = INF
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0 and C[(i,j)] == ones:
                        best = min(best, dst[i][j])
            return best if best != INF else -1

