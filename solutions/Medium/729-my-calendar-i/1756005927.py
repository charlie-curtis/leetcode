class MyCalendar:

    def __init__(self):

        self.sd = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.sd.bisect_right(startTime) -1
        if idx != -1:
            #check the meeting BEFORE US
            otherEnd = self.sd.peekitem(idx)[1]
            if otherEnd > startTime:
                #meeting before us didn't end in time
                return False
        if idx+1 < len(self.sd):
            #check the meeting AFTER US
            otherStart = self.sd.peekitem(idx+1)[0]
            if endTime > otherStart:
                return False
        self.sd[startTime] = endTime
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)