class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:


        if goal == start: return 0
        seen = set()
        q = deque()
        q.append([start, 0])
        seen.add(start)

        while len(q):

            #print(q)
            v, steps = q.popleft()
            
            for y in nums:
                for z in [v-y, v+y, v^y]:
                    if z not in seen:
                        if z == goal:
                            return steps+1
                        if z < 0 or z > 1000:
                            continue
                        seen.add(z)
                        q.append([z, steps+1])
        return -1