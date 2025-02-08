class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, target: int) -> int:

        avoid = set(forbidden)


        pq = deque()
        pq.append([0, 0, True])


        seen = set()
        seen.add((0, True))

        if target == 0:
            return 0

        #print("cutoff is", target+b)
        while pq:
            cost, x, avail = pq.popleft()

            #print("I'm at", x)
            if x in avoid:
                continue
            if x == target:
                return cost
            if x > 10**5:
                continue

            if avail and x - b >= 0 and (x-b, False) not in seen:
                seen.add((x-b, False))
                pq.append([cost+1, x-b, False])

            if (x+a, True) not in seen:
                seen.add((x+a, True))
                pq.append([cost+1, x+a, True])


        return -1
            
                         