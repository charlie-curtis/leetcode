class NumberContainers:

    def __init__(self):
        self.d = {}
        self.sls = defaultdict(SortedList)
        

    def change(self, index: int, number: int) -> None:
        if index in self.d:
            v = self.d[index]
            sl = self.sls[v]
            i = sl.bisect_left(index)
            del sl[i]
        
        self.d[index] = number
        self.sls[number].add(index)
        

    def find(self, number: int) -> int:
        sl = self.sls[number]
        if len(sl) == 0:
            return -1
        return sl[0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)