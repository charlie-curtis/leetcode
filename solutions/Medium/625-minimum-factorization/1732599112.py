class Solution:
    def smallestFactorization(self, n: int) -> int:

        if n == 1:
            return 1
        high = 2**31-1
        out = ""
        for i in range(9,1, -1):
            while n % i == 0:
                out+=str(i)
                n//=i
        
        if n != 1:
            return 0
        
        can = int(out[::-1])
        return can if can <= high else 0
        