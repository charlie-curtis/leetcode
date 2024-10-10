class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        for x in s:
            if x == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)
        return len(stack)
        

        #(()))