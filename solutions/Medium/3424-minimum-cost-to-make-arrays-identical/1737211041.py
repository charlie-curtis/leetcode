class Solution:
    def minCost(self, A: List[int], B: List[int], k: int) -> int:

        if A == B:
            return 0


        #cost if you only use x operation

        best = 0
        for a,b in zip(A,B):
            best+=abs(a-b)

        #cost if you use 1 k operation, then remaining x operations
        can = k
        A.sort()
        B.sort()

        for a,b in zip(A,B):
            can+=abs(a-b)

        return min(can, best)
        