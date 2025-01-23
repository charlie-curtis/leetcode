class Solution:
    def closestDivisors(self, num: int) -> List[int]:


        def sieve(n):

            best = 1e15
            x = 1
            ans = [-1,-1]
            while x*x <= n:
                if n %x == 0:
                    d = n//x
                    if abs(x-d) < best:
                        best = abs(x-d)
                        ans = [d,x]
                x+=1
            return ans 


        a = sieve(num+1)
        b = sieve(num+2)
        if abs(a[0] - a[1]) < abs(b[0] - b[1]):
            return a
        return b
        