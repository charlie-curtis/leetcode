class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        NEGINF = -1 * 10**9
        @cache
        def dp(i,j,k,l):
            if max([i,k]) == m or max([j,l]) == n:
                return NEGINF
            
            if min(grid[i][j], grid[k][l]) == -1:
                return NEGINF

            score = grid[i][j]
            score+= grid[k][l] if (i,j) != (k,l) else 0

            if (i == k == m-1) and (j == l == n-1):
                return score

            return max([
                dp(i+1, j, k+1, l),
                dp(i, j+1, k+1, l),
                dp(i, j+1, k, l+1),
                dp(i+1, j, k, l+1)
            ]) + score

        return max(0,dp(0,0,0,0))
                            