class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)

        in_progress = []
        meetings.sort()
        C = Counter()
        t = 0
        for start,end in meetings:
            duration = end-start
            start = max(t,start)
            if not rooms:
                #if there aren't any rooms available, increase the start time to handle the room
                #reclaiming process
                start = max(in_progress[0][0], start)
            while in_progress and in_progress[0][0] <= start:
                #reclaim any rooms that have ended
                _,r = heapq.heappop(in_progress)
                heapq.heappush(rooms,r)

            #pick the smallest room available
            r = heapq.heappop(rooms)
            C[r]+=1
            heapq.heappush(in_progress, [start+duration, r])
            t = max(t, start)
        
        mx = max(C.values())
        for i in range(n):
            if C[i] == mx:
                return i