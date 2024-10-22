class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heapq.heapify(sticks)

        pq = sticks
        ans = 0
        while len(pq) > 1:
            a,b = heapq.heappop(pq), heapq.heappop(pq)
            ans+=a+b
            heapq.heappush(pq, a+b)
        return ans
        