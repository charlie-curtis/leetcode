class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        n = len(weight)
        weight.sort()
        pref = list(accumulate(weight))
        return bisect_right(pref, 5000)
        