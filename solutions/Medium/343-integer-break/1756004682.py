class Solution:
    def integerBreak(self, n: int) -> int:

        #some kind of greedy logic

        #choose small numbers

        #4 = 2*2
        #5 = 2*3
        #6 = 3*3 (instead of 2*2*2)
        #7 = 3*2*2 (instead of 3*3*1)
        #8 = 3*3*2 (instead of 2*2*2)
        #you would never choose 4 (because that is just  = 2*2)
        #you would never choose 5 (because 2*3 has the same sum but higher multi)

        #so greedily choose 3 unless that would lock you into 3*1 (at which point you'd choose 2*2)

        R = n % 3
        #if R == 0, use all 3s
        #if R = 2, use all 3s and one 2
        #if R == 1, use 2*2, and the rest 3s

        if n == 2:
            return 1
        if n == 3:
            return 2
        if R == 0:
            #all 3s
            return 3**(n//3)
        if R == 1:
            #2*2, rest 3s
            return 4 * 3**(n//3 - 1)
        if R == 2:
            #2, rest 3s
            return 2*3**(n//3)

        raise ValueError("Wrong")
        