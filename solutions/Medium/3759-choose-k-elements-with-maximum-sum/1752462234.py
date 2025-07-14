class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        n = len(nums1)

        H = defaultdict(list)
        for i in range(n):
            H[nums1[i]].append([nums2[i], i])

        out = [0]*n
        ssum = 0
        pq = []
        for key in sorted(H.keys()):
            V = []
            for val, idx in H[key]:
                out[idx] = ssum
                V.append(val)
            
            for v in V:
                heapq.heappush(pq, v)
                ssum+=v
                if len(pq) > k:
                    ssum-=heapq.heappop(pq)
        return out