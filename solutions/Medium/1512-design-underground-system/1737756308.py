class UndergroundSystem:

    def __init__(self):
        self.d = {}
        self.state = {}
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.state[id] = [stationName, t]
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        fromStation, originalTime = self.state[id]
        del self.state[id]
        kkey = (fromStation, stationName)
        if kkey not in self.d:
            self.d[kkey] = [1, t-originalTime]
        else:
            curcnt, curtime = self.d[kkey]
            self.d[kkey] = [curcnt+1, curtime+(t-originalTime)]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cnt, time = self.d[(startStation,endStation)]
        return time/cnt
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)