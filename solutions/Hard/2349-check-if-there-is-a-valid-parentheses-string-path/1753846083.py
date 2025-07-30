class Solution:
    def hasValidPath(self, g: List[List[str]]) -> bool:
        m,n = len(g),len(g[0])

        @cache
        def dp(i,j, b):
            if min(i,j) < 0 or i == m or j == n:
                return False
            
            c = g[i][j]
            if c == '(':
                b+=1
            else:
                b-=1
            if b < 0:
                return False
            
            if (i,j) == (m-1, n-1):
                return b == 0
            
            return dp(i+1,j,b) or dp(i,j+1,b)
        
        res = dp(0,0,0)
        dp.cache_clear()
        return res