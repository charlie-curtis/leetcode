class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:

        #DIGIT DP - handling the d=0 case was a little tricky. The basic idea is we want to make
        #sure that we're not counting leading zero's. E.g. "009" should not be counted.

        #digit DP can be used to quickly count how many numbers are less than a very large number (e.g. imagine there is a number with 10^5 digits that can't be read entirely into memory). The number returned can be thought of as "paths", and we need to filter those paths for cases where they have a "d" in it. That is why this algorithm is keeping two separate counts -- one is the number of paths, and the other is the actual answer we're looking for
        @cache
        def count(s,i=0, tight=True, leadingZero = False):
            n=len(s)
            if i == n:
                return [1,0]
            cutoff = 9 if not tight else int(s[i])
            paths = 0
            special = 0
            for j in range(cutoff+1):
                cnt, prevSpecial = count(s,i+1, tight and j == int(s[i]), leadingZero & (j == 0))
                paths+=cnt
                special+=prevSpecial
                if j == d and (d != 0 or not leadingZero or (i == n-1)):
                    special+=cnt
            return [paths, special]

        a = count(str(high),0, True, True)
        b = count(str(low-1),0, True, True)

        return a[1] - b[1]
