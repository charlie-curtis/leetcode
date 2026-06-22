class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        d = defaultdict(int)

        for start,end,dir in shifts:
            if dir == 0:
                dir = -1
            d[start]+=dir
            d[end+1]-=dir

        cur = 0
        n = len(s)
        out = []
        for i in range(n):
            cur+=d[i]
            v = ord(s[i]) - ord('a')
            v+=cur
            v%=26
            c = chr(v + ord('a'))
            out.append(c)

        return ''.join(out)


        