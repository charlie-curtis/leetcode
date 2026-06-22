class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        n = len(workerTimes)
        multipliers = [1]*n

        pq = []
        for i in range(n):
            heapq.heappush(pq, [workerTimes[i], i])



        ans = 0
        while mountainHeight > 0:
            ans, i = heapq.heappop(pq)

            #reduce the height by 1
            mountainHeight-=1

            multipliers[i]+=1
            multi = multipliers[i]
            nxt_val = workerTimes[i]*multi
            heapq.heappush(pq, [nxt_val + ans, i])

        return ans 


        