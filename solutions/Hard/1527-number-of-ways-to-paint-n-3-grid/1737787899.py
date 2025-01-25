class Solution:
    def numOfWays(self, n: int) -> int:


        moves = []
        def bt(cur):
            if len(cur) == 3:
                moves.append(tuple(cur))
                return
            for i in range(3):
                if not cur or cur[-1] != i:
                    cur.append(i)
                    bt(cur)
                    cur.pop()

        bt([])

        MOD = 10**9 +7
        @cache
        def dp(i, prev):
            if i == n:
                return 1 

            ans = 0
            for j in range(len(moves)):
                good = True
                if prev != -1:
                    for k in range(3):
                        if moves[j][k] == prev[k]:
                            good = False
                            break
                if good:
                    ans+=dp(i+1, moves[j])
                    ans%=MOD
                            
            return ans
        return dp(0, -1)
                    
        