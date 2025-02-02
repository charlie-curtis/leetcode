class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        A = [x%2 for x in arr]

        n = len(A)
        for i in range(n-2):
            if A[i] == A[i+1] == A[i+2] == 1:
                return True
        return False
        