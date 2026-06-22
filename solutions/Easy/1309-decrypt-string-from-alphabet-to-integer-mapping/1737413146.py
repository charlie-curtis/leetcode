class Solution:
    def freqAlphabets(self, s: str) -> str:

        out = ""
        d = deque([x for x in s])
        while d:
            if len(d) >= 3 and d[2] == '#':
                v = int(d[0])*10 + int(d[1])
                out+=chr(ord('a') + v - 1)
                d.popleft()
                d.popleft()
                d.popleft()
            else:
                v = int(d[0])
                out+=chr(ord('a')+ v - 1)
                d.popleft()
        return out
            
        