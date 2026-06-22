class Solution:
    def canMakeArithmeticProgression(self, A: List[int]) -> bool:

        A.sort()
        B = zip(A, A[1:])

        seen = set()
        for a,b in B:
            seen.add(b-a)
        return len(seen) == 1

        
        