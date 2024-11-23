class Solution:
    def findBlackPixel(self, grid: List[List[str]], target: int) -> int:

        row_count = Counter()
        col_count = Counter()
        col_hash = defaultdict(set)
        m,n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                row_hash = hash(''.join(grid[i]))
                if grid[i][j] != 'B':
                    continue

                row_count[i]+=1
                col_count[j]+=1
                col_hash[j].add(row_hash)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'B':
                    continue
                if col_count[j] == row_count[i] == target and len(col_hash[j]) == 1:
                    ans+=1
        return ans

        