class OrderedStream:

    def __init__(self, n: int):
        self.sl = SortedList()
        self.expected = 1
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.sl.add((idKey, value))
        out = []
        sl = self.sl
        while len(sl) > 0 and sl[0][0] == self.expected:
            idx,v = sl.pop(0)
            out.append(v)
            self.expected+=1
        return out
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)