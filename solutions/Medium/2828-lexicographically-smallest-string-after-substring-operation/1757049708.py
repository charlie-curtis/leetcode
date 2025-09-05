class Solution:
    def smallestString(self, s: str) -> str:

        n = len(s)
        if s == 'a'*n:
            return 'a'*(n-1) + 'z'

        
        start = -1
        for i,x in enumerate(s):
            if x != 'a':
                start = i
                break
        

        end = start+1
        while end < n and s[end] != 'a':
            end+=1
        
        out = []
        for i,x in enumerate(s):
            if start <= i < end:
                c = chr(ord(x) - 1)
            else:
                c = x
            out.append(c)
        return ''.join(out)



