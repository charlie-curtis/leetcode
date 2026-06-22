class Solution:
    def minimumOperationsToMakeEqual(self, start: int, y: int) -> int:


        if start <= y:
            return y-start
        q = deque()
        q.append(start)

        seen = set()

        cost = 0
        while len(q):

            for _ in range(len(q)):
                x = q.popleft()
                if x == y:
                    return cost
    
    
                options = [x+1, x-1]
                for t in [5,11]:
                    if x%t == 0:
                        options.append(x//t)
                for v in options:
                    if v in seen:
                        continue
                    seen.add(v)
                    q.append(v)
            cost+=1
        return -1