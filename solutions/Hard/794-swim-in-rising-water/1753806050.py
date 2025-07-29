class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:

        n = len(g)

        l = 0
        r = n*n

        def dfs(i,j,seen, mid):
            if min(i,j) < 0 or max(i,j) >= n:
                return False
            if (i,j) in seen:
                return False
            if g[i][j] > mid:
                return False
            if i == j == n-1:
                return True
            seen.add((i,j))
            return any([
                    dfs(i+1, j, seen, mid),
                    dfs(i-1, j, seen, mid),
                    dfs(i, j+1, seen, mid),
                    dfs(i, j-1, seen, mid)
            ])


        while l <= r:
            mid = l + (r-l)//2
            if dfs(0,0,set(), mid):
                r = mid -1
            else:
                l = mid + 1
        return l
        