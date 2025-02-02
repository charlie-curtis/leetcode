class Solution:
    def makeGood(self, s: str) -> str:


        d = deque(s)
        found =True 
        while found:
            out = deque()
            found = False
            while len(d) > 0:
                if len(d) == 1:
                    out.append(d.pop())
                elif d[0].lower() == d[1].lower() and d[0] != d[1]:
                    found = True
                    d.popleft()
                    d.popleft()
                else:
                    out.append(d.popleft())

            d = out
            
        return ''.join(list(d))
        