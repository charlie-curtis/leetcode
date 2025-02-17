from sortedcontainers import SortedDict
class MRUQueue:

    def __init__(self, n: int):
        self.nxt_id = n+1
        self.sd = SortedDict()
        for i in range(1,n+1):
            self.sd[i] = i

    def fetch(self, k: int) -> int:
        _, val = self.sd.popitem(k-1)
        self.sd[self.nxt_id] = val
        self.nxt_id+=1
        return val
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)