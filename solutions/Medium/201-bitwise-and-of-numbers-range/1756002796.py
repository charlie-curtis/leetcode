class Solution:
    def rangeBitwiseAnd(self, low: int, high: int) -> int:

        out = 0
        #iterate through all the bits of LOW. If a bit is set to 1, find the next number that is greater than LOW that has this bit set to 0. If that number is less than HIGH, then we know that the bit will be a 0 in the final answer
        for i in range(32):
            x = 1<<i
            if x & low:
                #this bit is currently set, zero out all lte this one and add x*2
                y = (low >> (i+1)) << (i+1)
                y+=2*x
                if y > high:
                    out|=x
        return out



        