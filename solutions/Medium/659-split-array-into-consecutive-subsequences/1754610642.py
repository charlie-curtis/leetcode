class Solution:
    def isPossible(self, nums: List[int]) -> bool:


        #1,2,3,4,5
        #     , ,5,6

        pq = []
        for x,g in groupby(nums):
            L = len(list(g))
            tmp = []
            if pq and pq[0][1] + 1 != x:
                #the last group cannot match with this one, so validate it & empty it
                if pq[0][0] < 3:
                    return False
                pq = []
            while L and pq: #extend previous values, starting with the smallest segments
                L-=1
                cnt,_ = heapq.heappop(pq)
                heappush(tmp, [cnt+1,x])
            if pq and pq[0][0] < 3: #if we couldn't extend all the segments, then the orphaned ones must be length >= 3
                return False
            for _ in range(L): #start new segments if we must
                heapq.heappush(tmp, [1, x])
            pq = tmp
        
        return pq[0][0] >= 3 #last segment must be valid