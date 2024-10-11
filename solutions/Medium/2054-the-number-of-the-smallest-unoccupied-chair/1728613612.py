class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        target_arrival = times[targetFriend][0]

        times = deque(sorted(times))
        nxt_free = 0
        recycled = []
        pq = []

        while times:
            #process the next time
            t, d = times.popleft()

            #remove any departures that would have happened before or equal to this time
            #and mark the ID as available to use
            while pq and pq[0][0] <= t:
                _, id = heapq.heappop(pq)
                heapq.heappush(recycled, id)

            nxt_id = -1
            if recycled:
                #if there is an ID available, use it
                nxt_id = heapq.heappop(recycled)
            else:
                #else there isn't an ID available, so assign a new one
                nxt_id = nxt_free
                nxt_free+=1

            if t == target_arrival:
                #if this is our target friend, return the ID they get
                return nxt_id
            
            heapq.heappush(pq, [d, nxt_id])
        
        raise ValueError('Wrong')
            



        