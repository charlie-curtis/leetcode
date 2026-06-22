class Solution:
    def kthSmallestPath(self, dest: List[int], k: int) -> str:


        m,n = dest
        def dp(i,j, memo):
            if min(i,j) < 0 or i == m +1 or j == n + 1:
                return 0

            if (i,j) == (m,n):
                memo[(i,j)] = 1
                return 1
            if (i,j) in memo:
                return memo[(i,j)]


            res = dp(i+1, j, memo) + dp(i, j+1, memo)
            memo[(i,j)] = res
            return res



        memo = {}
        res = dp(0,0, memo)
        i,j = [0,0]
        out = []
        while [i,j] != dest:
            a = 0 if (i, j+1) not in memo else memo[(i, j+1)] #represents moving RIGHT "H"
            b = 0 if (i+1,j) not in memo else memo[(i+1,j)] #represents moving DOWN "V"


            if 0 < a >= k:
                out.append("H")
                j+=1
            else:
                k-=a
                out.append("V")
                i+=1

        return ''.join(out)

            
                
        