class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        d = defaultdict(deque)
        pq = []
        for i,x in enumerate(rains):
            d[x].append(i)


        out = []
        state = defaultdict(int)
        for i,x in enumerate(rains):
            if len(d[x]) > 0 and d[x][0] == i:
                d[x].popleft()
            if x == 0:
                if len(pq) > 0:
                    _, x = heapq.heappop(pq)
                    out.append(x)
                    state[x] = 0
                else:
                    out.append(1)
            else:
                if state[x] == 1:
                    return []
                state[x] = 1
                if len(d[x]) > 0:
                    heapq.heappush(pq, [d[x].popleft(), x])
                out.append(-1)
        return out
        