class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:


        stack = deque()
        ans = -1e15 
        minq = []
        #-y-x
        for x,y in points:
            while minq and abs(minq[0][1] - x) > k:
                heappop(minq)

            if minq:
                ans = max(ans, abs(minq[0][1]-x) + y+minq[0][2])
            heappush(minq, [x-y, x,y])

        return ans