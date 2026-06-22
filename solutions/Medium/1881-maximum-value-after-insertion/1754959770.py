class Solution:
    def maxValue(self, n: str, x: int) -> str:

        #scan left to right. If negative, we want to minimize
        #the negativity, so if x < nums[i], insert it before

        #what about equal? -1,3,5,1,7 x=5 -> ignore it and go off the next number
        
        #if positive, want to maximize, so if x > nums[i], insert it

        #7,8,3, x=1 else insert it at end

        isNeg = n[0] == '-'

        if isNeg:
            for i in range(1,len(n)):
                if x < int(n[i]):
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        for i in range(len(n)):
            if x > int(n[i]):
                return n[:i] + str(x) + n[i:]
        return n + str(x)
        