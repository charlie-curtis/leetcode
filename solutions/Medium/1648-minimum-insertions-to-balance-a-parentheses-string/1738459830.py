class Solution:
    def minInsertions(self, s: str) -> int:

        n = len(s)
        ans = 0
        stack = []

        i = 0
        while i < n:
            if s[i] == '(':
                stack.append('(')
            else:
                if i+1 == n or s[i+1] != ')':
                    ans+=1
                else:
                    #need to increment i an extra
                    i+=1
                if not stack:
                    ans+=1
                else:
                    stack.pop()

            
            i+=1
        while stack:
            stack.pop()
            ans+=2
        return ans
        