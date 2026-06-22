class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:

        #so you absolutely cannot go any further if you encounter a value that is >= you
        #however, even the values between you and that endpoint are not all visible

        #10 6 5 4 6 8 11

        #by the time we process 6, we'll see [5,6,8,11]
        #by the time we process 10, the stack will look like [6,6,8,11] which is the answer we want

        #mono inc stack
        m,n = len(heights), len(heights[0])

        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            stack = []
            for j in range(n-1, -1, -1):
                cnt = 0
                prev = -1
                while stack and heights[i][stack[-1]] < heights[i][j]:
                    cur = heights[i][stack.pop()]
                    if cur != prev:
                        cnt+=1
                    prev = cur
                if stack:
                    cnt+=1
                
                ans[i][j] = cnt
                stack.append(j)

        for i in range(n):
            stack = []
            for j in range(m-1, -1, -1):
                cnt = 0
                prev = -1
                while stack and heights[stack[-1]][i] < heights[j][i]:
                    cur = heights[stack.pop()][i]
                    if cur != prev:
                        cnt+=1
                    prev = cur
                if stack:
                    cnt+=1
                ans[j][i]+= cnt
                stack.append(j)

        return ans

        