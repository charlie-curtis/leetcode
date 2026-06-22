class SnapshotArray:

    def __init__(self, length: int):
        self.A = [SortedDict() for _ in range(length)]
        for i in range(length):
            self.A[i][0] = 0
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.A[index][self.i] = val
        

    def snap(self) -> int:
        self.i+=1
        return self.i-1
        

    def get(self, index: int, snap_id: int) -> int:
        sd = self.A[index]
        idx = sd.bisect_right(snap_id)-1
        return sd.peekitem(idx)[1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)