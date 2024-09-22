class MovingAverage:

    def __init__(self, size: int):
        self.sz = size
        self.vals = deque()
        self.summ = 0
        

    def next(self, val: int) -> float:
        self.vals.append(val)
        self.summ+=val
        if len(self.vals) > self.sz:
            removed = self.vals.popleft()
            self.summ-=removed
        return self.summ / len(self.vals)


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)