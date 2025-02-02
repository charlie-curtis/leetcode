class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:


        seen = set()

        m,n = len(grid), len(grid[0])
        def dfs(i,j, p,char):
            #print("called", i,j, "from", p)

            if i < 0 or j < 0 or i == m or j == n:
                return False
            if grid[i][j] != char:
                return False

            if (i,j) == p:
                return False
            if (i,j) in seen:
                #print("Found at", i,j, "and parent was", p)
                return True
            #print("adding to set")
            seen.add((i,j))

            dirs = [[-1,0], [1,0], [0,1], [0,-1]]
            nxt = [(i+a, j+b) for (a,b) in dirs]
            for ni,nj in nxt:
                if (ni,nj) != p and dfs(ni,nj, (i,j), grid[i][j]):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if (i,j) not in seen:
                    #print("starting dfs from", i,j)
                    res = dfs(i,j, (-1, -1), grid[i][j])
                    if res: return True
        return False
        