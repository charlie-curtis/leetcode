class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:


        if digit1 == digit2 == 0:
            return -1

        digit1, digit2 = min(digit1,digit2), max(digit1,digit2)
        q = deque()
        q.append(digit1)
        q.append(digit2)

        while q:
            x = q.popleft()
            if x > 2**31-1:
                return -1
            if x > k and x%k == 0:
                return x
            a,b = x*10+digit1, x*10+digit2
            if a != x:
                q.append(a)
            if b != x:
                q.append(b)