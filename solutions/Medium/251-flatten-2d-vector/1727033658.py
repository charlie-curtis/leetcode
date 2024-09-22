class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.i = 0
        self.j = 0
        self.vec = [x for x in vec if len(x)]
        self.empty = False

        

    def next(self) -> int:
        res = self.vec[self.i][self.j]
        self.scanNext()
        return res
        

    def hasNext(self) -> bool:
        return self.i != len(self.vec)

    def scanNext(self):
        n = len(self.vec)
        if not self.hasNext():
            return
        
        m = len(self.vec[self.i])
        if self.j+1 == m:
            self.i+=1
            self.j = 0
        else:
            self.j+=1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()