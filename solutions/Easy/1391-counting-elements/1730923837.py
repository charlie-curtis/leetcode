class Solution:
    def countElements(self, arr: List[int]) -> int:

        return sum([1 if x+1 in set(arr) else 0 for x in arr])
        