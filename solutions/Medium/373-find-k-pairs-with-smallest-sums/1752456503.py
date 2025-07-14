class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        m = len(nums1)
        n = len(nums2)


        pq = []
        for i in range(min(m,k)):
            heapq.heappush(pq, [nums1[i] + nums2[0], i, 0])
        
        out = []
        while len(out) < k:
            _, i,j = heapq.heappop(pq)
            out.append([nums1[i], nums2[j]])
            if j+1 < n:
                heapq.heappush(pq, [nums1[i] + nums2[j+1], i, j+1])
        return out
