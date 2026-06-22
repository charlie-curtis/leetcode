class Solution:
    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:


        m,n = len(grid), len(grid[0])
        ans = []
        def dfs(i,j,v, seen, path):
            if i < 0 or j < 0 or i == m or j == n or (i,j) in seen:
                return False
            
            val = grid[i][j]
            if val != 0 and val != v:
                return False
            
            seen.add((i,j))
            path.append([i,j])
            if len(seen) == m*n:
                nonlocal ans
                ans = path
                return True
            
            if v == val:
                v+=1
            
            dirs = [[-1,0], [1,0], [0,1], [0,-1]]
            for t1,t2 in dirs:
                ni = t1+i
                nj = t2+j
                res = dfs(ni,nj,v, seen, path)
                if res:
                    return True
            seen.remove((i,j))
            path.pop()
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,1,set(), []):
                    return ans
        return [] 
        