class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        return max([[sqrt(l**2 + w**2),l*w] for l,w in dimensions])[1]
        