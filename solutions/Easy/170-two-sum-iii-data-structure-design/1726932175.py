class TwoSum:

    def __init__(self):
        self.d = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.d[number]+=1
        

    def find(self, value: int) -> bool:
        for x in self.d.keys():
            t = value - x
            if t == x and self.d[x] > 1:
                return True
            elif t != x and t in self.d:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)