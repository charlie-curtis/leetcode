class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:


        m,n = len(board), len(board[0])

        MOD = 10**9 + 7
        @cache
        def dp(i,j):
            if i < 0 or j < 0 or board[i][j] == 'X':
                return [-1e15,-1e15]
            if i == 0 and j == 0:
                return [0,1]

            me = 0 if i == m-1 and j == n-1 else int(board[i][j])

            a,b = dp(i-1, j)
            c,d = dp(i, j-1)
            e,f = dp(i-1, j-1)
            best = max(a,c,e)

            paths = 0
            if a == best:
                paths+=b
            if c == best:
                paths+=d
            if e == best:
                paths+=f
            paths%=MOD
            return [best+me,paths]
        
        res = dp(m-1, n-1)
        if res[0] < 0:
            return [0,0]
        return res