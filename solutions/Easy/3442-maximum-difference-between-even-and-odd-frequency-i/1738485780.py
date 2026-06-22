class Solution:
    def maxDifference(self, s: str) -> int:

        C = Counter(s)
        maxOdd = max([v for v in C.values() if v % 2 == 1])
        minEven = min([v for v in C.values() if v % 2 == 0])

        return maxOdd - minEven