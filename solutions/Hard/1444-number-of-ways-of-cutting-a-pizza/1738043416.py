class Solution:
    def ways(self, mat: List[str], k: int) -> int:


        m,n = len(mat), len(mat[0])
        pref = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                a = pref[i+1][j]
                b = pref[i][j+1]
                c = pref[i][j]
                pref[i+1][j+1] = a + b - c + int(mat[i][j] == 'A')
        def get(r, c):
            return pref[r+1][c+1]
        def query(r1, c1, r2, c2):
            if r1 > r2 or c1 > c2:
                raise ValueError("invalid query")
            #r1, c1 (A)      #r1,c2 (B)


            #r2, c1 (C)     #r2,c2 (D)
            a = get(r1-1,c1-1)
            b = get(r1-1,c2)
            c = get(r2,c1-1)
            d = get(r2,c2)
            res = d + a - c - b
            return res

        MOD = 10**9 + 7
        @cache
        def dp(i, j, rem):
            if rem == 1:
                #return 1
                return int(query(i,j, m-1,n-1) > 0)
            

            ans = 0
            for l in range(i+1, m):
                if query(i,j,l-1,n-1) > 0:
                    ans+=dp(l,j, rem-1)
                    ans%=MOD
            for l in range(j+1, n):
                if query(i,j,m-1,l-1) > 0:
                    ans+=dp(i,l, rem-1)
                    ans%=MOD
            return ans
        
        return dp(0,0,k)