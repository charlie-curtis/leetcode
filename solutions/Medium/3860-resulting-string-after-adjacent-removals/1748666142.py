class Solution:
    def resultingString(self, s: str) -> str:


        stack = []
        def consec(x,y):
            if abs(ord(x)-ord(y)) == 1:
                return True
            if sorted([x,y]) == ['a', 'z']:
                return True
            return False
        for x in s:
            if not stack or not consec(x,stack[-1]):
                stack.append(x)
            else:
                stack.pop()
        
        return "".join(stack)
        