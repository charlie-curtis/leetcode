class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        #imagine you have some n (say 107)
        #write out the powers of 3 less than 107: 1, 3, 9, 27, 81
        #observe that if you want any chance of summing to 27, you always have to greedily take the largest power of 3
        #that is smaller than your current target. In this example, if i didn't select 81, then the remaining powers of 3 (27, 9, 3, 1) dont even sum to 81, so they definitely don't could sum to 107
        i = 14
        while n > 0 and i >= 0:
            v = 3**i
            if n >= v:
                n-=v
            i-=1
        return n == 0


        #you could also just try every combination of numbers since 3^15 > n. There are 32k combinations (3^0, 3^1, 3^2, ..., 3^15)