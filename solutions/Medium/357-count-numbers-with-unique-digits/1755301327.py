class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:



        cutoff = 10**n
        ans = 0
        def bt(x):
            if x >= cutoff:
                return
            nonlocal ans
            ans+=1
            
            t = str(x)
            for y in range(0,10):
                if str(y) in t:
                    continue
                if (y == 0 and x != 0) or (y > 0):
                    bt(x*10 + y)
        bt(0)
        return ans

        