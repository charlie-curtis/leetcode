from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        ans = 0
        maxq = []
        minq = []
        valid = -1
        for i,x in enumerate(nums):
            for q in [maxq, minq]:
                while q and abs(x - abs(q[0][0])) > 2:
                    v, idx = heapq.heappop(q)
                    valid = max(valid, idx)

            heapq.heappush(maxq, [-x, i])
            heapq.heappush(minq, [x, i])
            ans+=(i-valid)

        return ans