class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)


        #algorithm goes like this
        #iterate from left to right. If nums[i] > 0, then we need to satisfy that requirement by either
        #a previously opened interval (which we track using cur) OR a new interval (which si being tracked in a priority queue)

        d = defaultdict(list)
        for start,end in queries:
            #for every interval, index by startTime => [endTimes]
            d[start].append(end)

        #this let's us know when we need to decrement our cur variable
        adjustments = defaultdict(int)

        cur = ans = 0
        pq = []
        for i in range(n):
            cur+=adjustments[i] #any previously opened intervals might close here
            for x in d[i]:
                #load up any end times that begin here
                heapq.heappush(pq, -x)
            if nums[i] > cur:
                #we need to open a new interval
                needed = nums[i] - cur
                while needed > 0: #we might still need to open new intervals to satisfy this index
                    if len(pq) == 0:
                        #if there aren't any intervals left to open, return -1
                        return -1
                    end = -heapq.heappop(pq)
                    if i > end:
                        #can't use this interval because it's stale
                        ans+=1 #since we didn't use it, increment our score
                        continue
                    else:
                        #we can use this interval
                        needed-=1
                        cur+=1
                        adjustments[end+1]-=1
        return ans + len(pq)

