class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        pq = gifts

        while pq and k > 0:
            x = -heapq.heappop(pq)

            t = floor(sqrt(x))
            if t != 0:
                heapq.heappush(pq, -t)
            k-=1

        if not pq:
            return 0
        return sum([abs(x) for x in pq])
        