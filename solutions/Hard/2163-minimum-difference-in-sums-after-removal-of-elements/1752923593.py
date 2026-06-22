class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        lows=[float('inf')]*n
        highs=[float('-inf')]*n

        pq=[]
        ssum=0
        for i,x in enumerate(nums):
            ssum+=x
            heapq.heappush(pq, -x)
            if len(pq)>n//3:
                ssum+=heapq.heappop(pq)
            lows[i]= ssum
        ssum=0
        pq=[]
        for i in range(n-1,-1,-1):
            x=nums[i]
            ssum+=x
            heapq.heappush(pq, x)
            if len(pq)>n//3:
                ssum-=heapq.heappop(pq)
            highs[i]= ssum
        ans=min([lows[i]-highs[i+1] for i in range(n//3-1,n-n//3)])
        return ans
            
            