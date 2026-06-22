class Solution:
    def numberOfCleanRooms(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        def is_next_invalid(i,j,dir):
            nxt_i, nxt_j = i + dir[0], j + dir[1]
            is_invalid = nxt_i == m or nxt_i < 0 or nxt_j == n or nxt_j < 0 or grid[nxt_i][nxt_j] == 1
            return is_invalid

        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        i= j= offset = 0
        seen = set()
        seen_with_dir = set()
        while True:
            dir = dirs[offset%4]
            key = (i,j,dir[0], dir[1])
            if key in seen_with_dir:
                break
            seen_with_dir.add(key)
            seen.add((i,j))
            before = offset 
            while is_next_invalid(i,j,dirs[offset%4]):
                if offset-before == 4:
                    return len(seen)
                offset+=1
            dir = dirs[offset%4]
            i,j = i+dir[0], j + dir[1]
            
        return len(seen)