class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.m = maxSize
        

    def push(self, x: int) -> None:
        m = self.m
        if len(self.stack) < m:
            self.stack.append([x, 0])


    def pop(self) -> int:
        if len(self.stack):
            v,adj = self.stack.pop()
            if self.stack:
                self.stack[-1][1]+=adj
            return v + adj
        return -1
        
        

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        l = len(self.stack)
        self.stack[min(l-1, k-1)][1]+=val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)