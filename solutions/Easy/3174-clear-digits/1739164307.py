class Solution:
    def clearDigits(self, s: str) -> str:
        out = []
        b = 0
        for x in s[::-1]:
            if x.isdigit():
                b+=1
            elif b == 0:
                out.append(x)
            else:
                b-=1
        return ''.join(out)[::-1]
        