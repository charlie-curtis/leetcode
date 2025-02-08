class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.state = []
        self.inc = 0
        self.m = 1

    def append(self, val: int) -> None:
        self.state.append([val, self.inc, self.m])

    def addAll(self, inc: int) -> None:
        self.inc+=inc

    def multAll(self, m: int) -> None:
        self.m*=m
        self.inc*=m
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.state):
            return -1


        a1, m1 = self.inc, self.m
        v, a2, m2 = self.state[idx]


        x = m1//m2
        y = a1 - a2*x
        #print("high/low add", a1,a2)
        #print("high/low multi", m1, m2)

        return  (y + v*x) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)