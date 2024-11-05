class Solution:
    def minProductSum(self, A: List[int], B: List[int]) -> int:

        A.sort()
        B.sort(reverse=True)

        combined = list(zip(A,B))

        return sum([x[0] * x[1] for x in combined])
        


        