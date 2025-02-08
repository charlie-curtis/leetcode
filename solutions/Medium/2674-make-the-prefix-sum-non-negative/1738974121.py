class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:

        n = len(nums)


        pq = []
        ssum = ans = 0
        for x in nums:
            ssum+=x
            heapq.heappush(pq, x)
            while ssum < 0:
                ans+=1
                ssum-=heapq.heappop(pq)
        return ans
