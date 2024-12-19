from datetime import datetime
from sortedcontainers import SortedDict
import calendar

class LogSystem:

    def __init__(self):
        self.sd = SortedDict()
        

    def get_days_in_month(self,year, month):
        return calendar.monthrange(year, month)[1]
    def to_timestamp(self, s, gran = None, isStart = True):
        year,month,day,hour, minute,second = [int(x) for x in s.split(":")]
        if gran == "Year":
            if isStart:
                month = day = 1
                hour = minute = second = 0
            else:
                month = 12
                day = self.get_days_in_month(year, month)
                hour = 23
                minute = second = 59
        elif gran == "Month":
            if isStart:
                day = 1
                hour = minute = second = 0
            else:
                day = self.get_days_in_month(year, month)
                hour = 23
                minute = second = 59

        elif gran == "Day":
            if isStart:
                hour = minute = second = 0
            else:
                hour = 23
                minute = second = 59
        elif gran == "Hour":
            if isStart:
                minute = second = 0
            else:
                minute = second = 59
        elif gran == "Minute":
            if isStart:
                second = 0
            else:
                second = 59
        print("creating a dt with", year,month,day,hour,minute,second)
        dt = datetime(year, month, day, hour, minute, second)
        return dt.timestamp()


    def put(self, id: int, timestamp: str) -> None:
        timestamp = self.to_timestamp(timestamp)
        if timestamp not in self.sd:
            self.sd[timestamp] = [id]
        else:
            self.sd[timestamp].append(id)
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        print("creating lower for", granularity, "with input", start)
        lower = self.to_timestamp(start, granularity)
        print("creating upper for", granularity, "with input", end)
        upper = self.to_timestamp(end, granularity, False)

        print(lower, upper)
        print(self.sd.keys())
        idx = self.sd.bisect_left(lower)
        out = []
        while idx < len(self.sd) and self.sd.peekitem(idx)[0] <= upper:
            out+= self.sd.peekitem(idx)[1]
            idx+=1
        return out

        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)