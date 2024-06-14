class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i,x in enumerate(arr):
            self.d[x].append(i)

        

    def query(self, left: int, right: int, value: int) -> int:
        l = self.d[value]
        a = bisect_right(l, left-1)
        b = bisect_right(l, right)

        # 1, 3 , 7, 10

        return b-a
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)