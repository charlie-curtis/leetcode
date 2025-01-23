class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        A = [[x.bit_count(), x] for x in arr]
        A.sort()
        return [x[1] for x in A]
        