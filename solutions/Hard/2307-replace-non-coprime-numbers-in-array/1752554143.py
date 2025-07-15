class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        stack=nums[::-1]
        fin = []

        while len(stack) >= 2:
            gval = gcd(stack[-1],stack[-2])
            if  gval == 1:
                fin.append(stack.pop())
                continue
            a,b = stack.pop(), stack.pop()
            mval = a*b//gval
            stack.append(mval)
            if fin:
                stack.append(fin.pop())
        if len(stack):
            fin.append(stack.pop())
        return fin