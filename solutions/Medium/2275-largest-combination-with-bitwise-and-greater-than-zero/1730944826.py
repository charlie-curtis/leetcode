class Solution:
    def largestCombination(self, can: List[int]) -> int:

        C = Counter()
        for x in can:
            i = 0
            while x > 0:
                C[i]+= x % 2
                x//=2
                i+=1



        return max(C.values())
        