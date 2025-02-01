class Solution:
    def countOdds(self, low: int, high: int) -> int:

        res = (high-low)//2

        if high % 2 == 1 or low % 2 == 1:
            res+=1
        return res


        #even - even - solved
        #odd -odd -> solved
        #even -odd 4 -7 (expected=2)
        #5-8 expected (2)
        