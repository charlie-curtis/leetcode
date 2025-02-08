class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pref = [0]*n
        if n == 1:
            return 0

        pq = []
        avail = []
        ssum = 0
        ups = 0
        for i in range(n):
            if i > 0 and heights[i-1] < heights[i]:
                #need to use bricks
                x = heights[i] - heights[i-1]
                heapq.heappush(pq, -x)
                ssum+=x
                ups+=1
                needed = ups - ladders
                    
            needed = ups - ladders
            if needed > 0:
                if len(avail) > 0:
                    v = heappop(avail)
                    ssum+=v
                    heappush(pq, -v)
                    
                while len(pq) > needed:
                    v = abs(heappop(pq))
                    ssum-=v
                    heappush(avail, v)
                pref[i] = ssum
            else:
                pref[i] = pref[i-1] if i > 0 else 0


        for i in range(1,n):
            if pref[i] < pref[i-1]:
                raise ValueError("Wrong")
        l = 0
        r = n-1

        #TTTFFFFFFFF
        while l <= r:
            mid = l + (r-l)//2
            if pref[mid] <= bricks:
                l = mid + 1
            else:
                r = mid -1
        return r