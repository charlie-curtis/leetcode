class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        best = 0
        left.sort()
        right.sort()
        if left:
            best = max(best, left[-1])
        if right:
            best = max(best, n-right[0])
        return best
        