class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {}
        d['}'] = '{'
        d[')'] = '('
        d[']'] = '['
        for x in s:
            if x not in '}])':
                stack.append(x)
                continue
            elif not stack or d[x] != stack[-1]:
                return False
            stack.pop()
        return not stack
            
        