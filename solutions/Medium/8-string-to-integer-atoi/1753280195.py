class Solution:
    def myAtoi(self, s: str) -> int:

        s= s.strip()
        if not s or (not s[0].isdigit() and s[0] not in '+-'):
            return 0
        neg = s[0] == "-"

        i = 0 if s[0].isdigit() else 1
        j = i
        n = len(s)
        out = 0
        low = -2**31
        high = 2**31-1
        while i < n and s[i].isdigit():
            out = out*10 + int(s[i])
            if neg and out >= high+1:
                return low
            if not neg and out >= high:
                return high
            i+=1

        return out if not neg else -out
