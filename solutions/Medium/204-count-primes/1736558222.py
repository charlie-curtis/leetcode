class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 1:
            return 0
        p = [True]*(n)
        p[0] = p[1] = False
        i = 2
        while i*i < n:
            if p[i]:
                j = 2
                while j*i < n:
                    p[i*j] = False
                    j+=1
            i+=1 if i == 2 else 2


        return sum([1 if x == True else 0 for x in p])

        