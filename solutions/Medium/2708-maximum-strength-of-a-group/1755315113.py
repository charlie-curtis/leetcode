class Solution:
    def maxStrength(self, nums: List[int]) -> int:

        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        zero = [x for x in nums if x == 0]

        if not pos and not neg:
            #there are no positive or negative numbers. Only 0
            return 0
        #There is only 1 negative number, no positive numbers
        if not pos and len(neg) == 1:
            #either return 0 or the negative number
            return neg[0] if not len(zero) else 0
        
        #else return the non-zero multiplied sum, possibly removing a negative number if needed
        T = reduce(lambda x,y: x*y, pos+neg)
        if T > 0:
            return T
        neg.sort()
        T//=neg[-1]
        return T
