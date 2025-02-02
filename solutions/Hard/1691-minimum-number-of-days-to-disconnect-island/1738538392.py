class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        #this is a tricky casework problem that i had to use hints for
        m, n = len(grid), len(grid[0])

        #if there is already > 1 island, return 0
        #else, there is only 1 island
        #you want to carve out up to 4 spaces in order to create an island (N,S,E,W). If you are only partially surrounded, then it costs fewer moves


        #the one exception is if there are 2 1's next to each other



        def dfs(i,j, seen):
            if i < 0 or j < 0 or i == m or j == n:
                return
            if grid[i][j] != 1:
                return
            if (i,j) in seen:
                return

            seen.add((i,j))
            #print("adding", i,j, "to set")
            
            dfs(i+1, j, seen)
            dfs(i-1, j, seen)
            dfs(i, j+1, seen)
            dfs(i, j-1, seen)


        def isconnected():
            seen = set()
            ccs = 0
            ones = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        ones+=1

                        if (i,j) not in seen:
                            #print("searching", i,j, seen)
                            dfs(i,j, seen)
                            ccs+=1
                            if ccs > 1:
                                return False
            if ones == 0:
                return False
            return True

        if not isconnected():
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not isconnected():
                        return 1
                    grid[i][j] = 1
        return 2

        #key insight i was missing is that we can brute for check for the "1 move case"
