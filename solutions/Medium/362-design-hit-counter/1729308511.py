from sortedcontainers import SortedList
class HitCounter:

    def __init__(self):
        self.sl = SortedList()
        

    def hit(self, timestamp: int) -> None:
        self.sl.add(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        high_idx = self.sl.bisect_right(timestamp)-1
        low_idx = self.sl.bisect_right(timestamp-300)-1

        return high_idx - low_idx
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)