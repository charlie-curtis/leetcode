class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.a = deque(v1)
        self.b = deque(v2)
        self.a_go = True
        

    def next(self) -> int:
        if not self.a:
            return self.b.popleft()
        if not self.b:
            return self.a.popleft()
        
        res = self.a.popleft() if self.a_go else self.b.popleft()
        self.a_go = not self.a_go
        return res

        

    def hasNext(self) -> bool:
        return self.a or self.b
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())