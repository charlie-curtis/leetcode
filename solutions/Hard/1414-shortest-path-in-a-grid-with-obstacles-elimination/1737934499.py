class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        dst = {}

        pq = [(0,0,0,0)]
        dst[(0,0,0)] = 0
        m, n = len(grid), len(grid[0])

        while pq:
            cost, i,j, used = heappop(pq)

            if (i,j,used) in dst and dst[(i,j,used)] < cost or used > k:
                continue

            if i == m-1 and j == n-1:
                return cost
            
            dirs = [[1,0], [0,1], [-1,0], [0,-1]]
            nxt = [(i+x, j+y) for x,y in dirs]
            for ni, nj in nxt:
                if ni < 0 or nj < 0 or ni == m or nj == n:
                    continue
                nu = used+1 if grid[ni][nj] == 1 else used
                g = (ni,nj,nu) not in dst or dst[(ni,nj,nu)] > cost+1
                if not g:
                    continue
                if (ni,nj, nu-1) in dst and dst[(ni,nj,nu-1)] <= cost + 1:
                    dst[(ni,nj,nu)] = dst[(ni,nj,nu-1)]
                    continue
                dst[(ni,nj,nu)] = cost+1
                heapq.heappush(pq, (cost+1,ni,nj,nu))
        return -1
        