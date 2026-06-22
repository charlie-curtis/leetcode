class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:


        pq = []
        for x in nums:
            heapq.heappush(pq, -x)

        
        ans = 0
        for i in range(k):
            x = abs(heapq.heappop(pq))
            ans+=x
            heapq.heappush(pq, -ceil(x/3))
        return ans


        

        