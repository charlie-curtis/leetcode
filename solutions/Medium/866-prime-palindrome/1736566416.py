class Solution:
    pal = set()
    def do(cur):
        if len(cur) > 9:
            return 

        if cur:
            v = int(''.join([x for x in cur]))
            Solution.pal.add(v)

        start = 0
        stop = 10
        for i in range(10):
            cur.appendleft(str(i))
            cur.append(str(i))
            Solution.do(cur)
            cur.pop()
            cur.popleft()
        
        if not cur:
            for i in range(10):
                cur.append(str(i))
                Solution.do(cur)
                cur.pop()
        
    
    def primePalindrome(self, n: int) -> int:

        if not self.pal:
            Solution.do(deque())
            Solution.pal = sorted(Solution.pal)
        
        def isPrime(n):
            if n == 1:
                return False

            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False
            return True



        idx = bisect_left(Solution.pal, n)
        while True:
            if isPrime(Solution.pal[idx]):
                return Solution.pal[idx]
            idx+=1
