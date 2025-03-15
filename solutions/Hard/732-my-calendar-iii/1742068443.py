class MyCalendarThree:

    def __init__(self):
        self.events = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> int:
        if startTime not in self.events:
            self.events[startTime] = 0
        if endTime not in self.events:
            self.events[endTime] = 0
        self.events[startTime]+=1
        self.events[endTime]-=1

        l = accumulate([v for v in self.events.values()])
        return max(l)

        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)