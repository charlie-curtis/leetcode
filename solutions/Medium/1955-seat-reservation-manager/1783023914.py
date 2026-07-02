class SeatManager:

    def __init__(self, n: int):
        self.sl = SortedList(range(1,n+1))
        

    def reserve(self) -> int:
        x = self.sl[0]
        del self.sl[0]
        return x
        

    def unreserve(self, seatNumber: int) -> None:
        self.sl.add(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)