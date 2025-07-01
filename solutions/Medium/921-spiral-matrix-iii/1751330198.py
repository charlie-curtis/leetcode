class Solution:
    def spiralMatrixIII(self, m: int, n: int, rStart: int, cStart: int) -> List[List[int]]:

        ans = []
        l = 0

        r,c = rStart, cStart
        def isgood(r,c):
            return (0 <= r < m) and (0 <= c < n)
        while len(ans) < m*n:

            #go right - increase l first
            l+=1
            for i in range(l):
                if len(ans) == m*n:
                    break
                if isgood(r,c):
                    ans.append([r,c])
                c+=1

            #go down
            for i in range(l):
                if len(ans) == m*n:
                    break
                if isgood(r,c):
                    ans.append([r,c])
                r+=1

            #go left  - increase l first
            l+=1
            for i in range(l):
                if len(ans) == m*n:
                    break
                if isgood(r,c):
                    ans.append([r,c])
                c-=1
            
            #go up
            for i in range(l):
                if len(ans) == m*n:
                    break
                if isgood(r,c):
                    ans.append([r,c])
                r-=1
        
        return ans
