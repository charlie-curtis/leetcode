class Solution:
    def maxDepth(self, s: str) -> int:

        ans = b = 0
        for x in s:
            if x == '(':
                b+=1
            elif x == ')':
                b-=1
            ans = max(ans, b)
        return ans
        