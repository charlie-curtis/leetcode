class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        q = deque(s)

        balance = 0
        for d,amt in shift:
            if d == 0:
                balance-=amt
            else:
                balance+=amt

        while balance > 0:
            q.appendleft(q.pop())
            balance-=1

        while balance < 0:
            q.append(q.popleft())
            balance+=1


        return ''.join(q)
        