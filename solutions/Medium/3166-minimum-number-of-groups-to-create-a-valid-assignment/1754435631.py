class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        #editorial

        A=Counter(balls).values()

        def check(x):
            best = 0
            for y in A:
                found = False
                can = 0
                for j in range(y//x, -1, -1):
                    R = y - x*j
                    if R == 0:
                        best+=j
                        found = True
                        break
                    elif (x-1 > 0) and (R % (x-1)) == 0:
                        found = True
                        best+= j + (R//(x-1))
                        break
                if not found:
                    return float('inf')
            return best

        mn=min(A)
        return min([check(x) for x in range(mn+1, 0, -1)])
