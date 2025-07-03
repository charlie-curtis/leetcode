class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)

        pq = []
        for i in range(1,n):
            pq.append([1/arr[i], i, 0])

        heapq.heapify(pq)
        
        cur = -1
        cnt = 0
        while cnt < k:
            _, i, j = heapq.heappop(pq)
            cnt+=1
            if cnt == k:
                return [arr[j],arr[i]]
            if j+1 < i:
                heapq.heappush(pq, [arr[j+1]/arr[i], i, j+1])
        return cur
            


        