class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)

        ans = [0]*n
        stack = [n-1]
        for i in range(n-2, -1, -1):
            cnt = 0
            while stack and heights[i] >= heights[stack[-1]]:
                idx = stack.pop()
                cnt+=1 if heights[idx] != heights[i] else 0
            if stack:
                cnt+=1
            stack.append(i)
            ans[i] = cnt
        return ans



        