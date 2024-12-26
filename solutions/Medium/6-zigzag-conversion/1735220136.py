class Solution:
    def convert(self, s: str, n: int) -> str:
        out = [""]*n
        
        if n == 1: return s
        
        dir = 1
        pos = 0
        for x in s:
            out[pos]+=x
            a = pos == 0 and dir == -1
            b = pos == n-1 and dir == 1
            if a or b:
                dir*=-1
            pos+=dir
        return "".join(out)