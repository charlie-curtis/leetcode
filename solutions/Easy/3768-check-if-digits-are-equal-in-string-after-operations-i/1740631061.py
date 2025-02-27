class Solution:
    def hasSameDigits(self, s: str) -> bool:

        q = [int(x) for x in s]

        while len(q) > 2:
            q1 = []
            for i in range(len(q)-1):
                r = q[i] + q[i+1]
                q1.append(r%10)
            q = q1

        return q[0] == q[1]


        