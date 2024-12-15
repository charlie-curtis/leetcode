class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        n = len(classes)
        pq = []
        for x,y in classes:
            can = (x+1)/(y+1)
            cur = x/y
            diff = can-cur
            pq.append([-diff, x,y])

        heapq.heapify(pq)

        while extraStudents > 0:
            _, x,y = heapq.heappop(pq)
            extraStudents-=1
            x+=1
            y+=1
            can = (x+1)/(y+1)
            cur = x/y
            diff = can-cur
            heapq.heappush(pq, [-diff, x,y])

        
        t=0
        for _, x,y in pq:
            t+=(x/y)
        
        return t/len(pq)


        