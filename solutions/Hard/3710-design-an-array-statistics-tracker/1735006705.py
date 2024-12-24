class StatisticsTracker:

    def __init__(self):
        self.numbers = deque() #all the active numbers
        self.ssum = 0 #total of all the nums in deque

        #frequency - used for quickly finding the mode
        self.freq = defaultdict(int)
        self.mode = SortedDict()
        self.sl = SortedList()
        
    
    def adjustFreq(self, x, isIncrement):

        #get cur_freq
        cur_freq = self.freq[x]

        #de-register from current mode
        if cur_freq in self.mode:
            sset = self.mode[cur_freq]
            sset.discard(x)
            if len(sset) == 0:
                del self.mode[cur_freq]

        new_freq = cur_freq + 1 if isIncrement else cur_freq - 1
        self.freq[x] = new_freq
        if new_freq not in self.mode:
            #print(self.mode)
            self.mode[new_freq] = set()

        self.mode[new_freq].add(x)

    def addNumber(self, x: int) -> None:
        self.numbers.append(x)
        self.ssum+=x

        self.adjustFreq(x, True)
        self.sl.add(x)

        

    def removeFirstAddedNumber(self) -> None:
        if not self.numbers:
            return
        x = self.numbers.popleft()
        self.ssum-=x
        self.adjustFreq(x, False)
        self.sl.remove(x)

        

    def getMean(self) -> int:
        if not self.numbers:
            return 0
        return self.ssum // len(self.numbers)
        

    def getMedian(self) -> int:
        n = len(self.sl)
        return self.sl[n//2]
        

    def getMode(self) -> int:
        sset = self.mode.peekitem(-1)[1]
        return min(sset)
        


# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()