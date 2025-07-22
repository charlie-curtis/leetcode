class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        def test(x):
            if x <= 1:
                return False
            for i in range(2, floor(sqrt(x))+1):
                if x % i == 0:
                    return False
            return True

        seen = set()
        #9,999,999,999
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                a = int(s[i:j+1])
                if test(a):
                    seen.add(a)
        
        A = sorted([x for x in seen], reverse=True)
        if len(A) < 3:
            return sum(A)
        return sum(A[:3])
        