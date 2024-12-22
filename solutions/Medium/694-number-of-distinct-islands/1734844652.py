class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:


        m,n = len(grid), len(grid[0])

        def dfs(i,j, seen):
            if i < 0 or j < 0 or i == m or j == n or (i,j) in seen or grid[i][j] != 1:
                return

            seen.add((i,j))

            dfs(i+1, j, seen)
            dfs(i-1, j, seen)
            dfs(i, j-1, seen)
            dfs(i, j+1, seen)



        def translate(seen):
            baseline = -1
            for x,y in seen:
                if baseline == -1 or x < baseline[0] or (x == baseline[0] and y < baseline[1]):
                    baseline = [x,y]

            out = []
            for x,y in seen:
                out.append((x-baseline[0], y - baseline[1]))
            out.sort()
            return tuple(out)
        

        allSeen = set()
        translatedSeen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in allSeen:
                    tmpSeen = set()
                    dfs(i,j, tmpSeen)
                    allSeen|=tmpSeen
                    kkey = translate(tmpSeen)
                    translatedSeen.add(kkey)
        return len(translatedSeen)
        