class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        m,n = len(land), len(land[0])

        def dfs(i,j, seen):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if land[i][j] == 0:
                return
            if (i,j) in seen:
                return
            
            seen.add((i,j))
            dfs(i+1, j, seen)
            dfs(i-1, j, seen)
            dfs(i, j-1, seen)
            dfs(i, j+1, seen)

        
        overall = set()

        ans = [] 
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i,j) not in overall:
                    seen = set()
                    dfs(i,j, seen)
                    small_x = 1e10
                    small_y = 1e10
                    large_x = -1e10
                    large_y = -1e10
                    for x,y in seen:
                        overall.add((x,y))
                        small_x = min(small_x, x)
                        large_x = max(large_x, x)
                        small_y = min(small_y, y)
                        large_y = max(large_y, y)
                    ans.append([small_x, small_y, large_x, large_y])
        return ans
                    

                    
        