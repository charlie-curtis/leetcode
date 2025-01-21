class TweetCounts:

    def __init__(self):
        self.d = defaultdict(SortedList)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.d[tweetName].add(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, tmpStart: int, endTime: int) -> List[int]:
        jump = 0
        if freq == "minute": jump = 60
        elif freq == "hour": jump = 3600
        elif freq == "day": jump = 86400
        else: raise ValueError("Wrong")

        out = []
        li = self.d[tweetName]
        start = tmpStart
        while start <= endTime:
            tEnd = min(endTime, start+jump-1)
            a = li.bisect_left(start)
            b = li.bisect_right(tEnd)-1
            
            res = b-a+1
            out.append(res)
            start = tEnd+1
        return out

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)