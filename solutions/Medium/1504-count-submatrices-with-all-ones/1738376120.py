class Solution:
    def numSubmat(self, grid: List[List[int]]) -> int:


        m,n = len(grid), len(grid[0])
        up = [[0 for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i-1 >= 0:
                        up[i][j] = up[i-1][j] + 1
                    else:
                        up[i][j] = 1
        ans = 0
        for i in range(m):
            ssum = 0
            #h, ssum, l
            stack = []
            for k in range(n):
                l1 = 1
                h1 = up[i][k]
                while stack and stack[-1][0] >= h1:
                    h2,l2 = stack.pop()
                    ssum-=h2*l2
                    l1+=l2
                ssum+=l1*h1
                print(ssum)
                ans+=ssum
                stack.append([h1, l1])
            print(" ")
        return ans


        return ans
        '''
        [[1,0,1],
         [1,1,0]
         [1,1,0]]
        '''