class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:

        n = len(grid)
        has = [n]*n
        for i in range(n):
            j = n-1
            cnt = 0
            while j >= 0 and grid[i][j] == 0:
                cnt+=1
                j-=1
            has[i] = cnt
        

        need = [n-1-i for i in range(n)]

        ans = 0
        for i in range(n):
            if has[i] >= need[i]:
                continue
            found = False
            for j in range(i+1,n):
                if has[j] >= need[i]:
                    ans+=(j-i)
                    found = True
                    has[i+1:j+1] = has[i:j]
                    break
            if not found:
                return -1

        return ans

        #2 1 0

        #need #3 2 1 0
        #has  #2 3 4 0