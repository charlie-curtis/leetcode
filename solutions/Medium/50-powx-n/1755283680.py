class Solution:
    def myPow(self, x: float, n: int) -> float:
        def do(x,n):
            if n == 0:
                return 1
        
            if n % 2 == 1:
                return x*do(x,n-1)
            R = do(x,n//2)
            return R*R

        flag = n < 0
        if flag:
            n = -n
        res = do(x,n)
        if flag:
            return 1/res
        return res


        