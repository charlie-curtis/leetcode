class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:


        #spent over an hour on this problem; looked at the editorial
        #takeaways
        #1.figure out how you're going to model the problem. Don't just randomly code something
        #the trickiness of the problem came from figuring out how to handle duplicates. Don't overthink it. Use open-closed intervals
        #also another takeaway, I didn't know i could model this like a interval intersection problem. that made it alot simpler

        delta = 1e-5

        intervals = []
        for i in range(len(y)-1):
            a,b= y[i], y[i+1]
            if i != 0:
                if a > b:
                    a-=delta
                else:
                    a+=delta
            intervals.append([min(a,b), max(a,b)])


        intervals.sort()
        #print(intervals)
        #return -1

        pq = []
        ans = 0
        
        offset = 0
        n = len(intervals)
        for i in range(n):
            start,end = intervals[i]

            #pop off anything that is out of our time window
            while pq and pq[0] < start:
                heapq.heappop(pq)

            heapq.heappush(pq, end)

            ans = max(ans, len(pq))

        return ans