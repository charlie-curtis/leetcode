class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        b = 0
        out = []

        for x in s:
            if x == '(':
                out.append(x)
                b+=1
            elif x == ')':
                if b > 0:
                    b-=1
                    out.append(x)
            else:
                out.append(x)
        
        f = []
        for x in out[::-1]:
            if x != '(' or b == 0:
                f.append(x)
            else:
                b-=1
        
        return ''.join(f[::-1])

        