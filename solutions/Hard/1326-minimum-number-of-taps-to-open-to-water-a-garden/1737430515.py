class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        pq = []
        ans = 0
        good_idx = -1
        starts = defaultdict(list)
        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue
            low, high = max(0, i-ranges[i]), min(n, i+ranges[i])
            starts[low].append((high, i))
        for i in range(n+1):
            for end,j in starts[i]:
                heapq.heappush(pq, (-end, j))
            if i < good_idx or good_idx == n:
                continue
            else:
                #we need to pull
                if not pq:
                    return -1
                good_idx, j = heapq.heappop(pq)
                good_idx = abs(good_idx)
                if good_idx < i:
                    return -1
                print("I opened the", j, "tap which will suffice until", good_idx, "Im currentl at", i)
                ans+=1
        return ans