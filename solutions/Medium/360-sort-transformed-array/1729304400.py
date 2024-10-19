class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        # The O(N) solution is to observe that this makes a parabola, and you can therefore use 2 pointers to find the smallest
        #it's a little bit tedious though because the parabola can also be upside down, in which case you need to work from the endpoints inwards. If the parabola is rightside up, then you need to work from the inflection point outwards
        return sorted([a*x**2 + b*x + c for x in nums])