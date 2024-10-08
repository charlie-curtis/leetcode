class StringIterator:

    def __init__(self, s: str):

        self.pairs = deque()
        locs = []
        for i,x in enumerate(s):
            if x.isalpha():
                locs.append(i)
        
        locs = list(zip(locs, locs[1:] + [len(s)]))

        for me, nxt in locs:
            num = int(s[me+1:nxt])
            char = s[me]
            self.pairs.append([char, num])
        

    def next(self) -> str:
        if not self.hasNext():
            return " "
        char, cnt = self.pairs.popleft()
        cnt-=1
        if cnt > 0:
            self.pairs.appendleft([char,cnt])
        return char
        

    def hasNext(self) -> bool:
        return len(self.pairs) > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()