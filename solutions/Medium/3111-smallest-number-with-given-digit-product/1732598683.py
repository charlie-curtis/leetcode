class Solution:
    def smallestNumber(self, n: int) -> str:

        C = Counter()
        if n == 1:
            return "1"
        for i in range(9,1, -1):
            while n % i == 0:
                n//=i
                C[i]+=1

        if n != 1:
            return "-1"

        stack = []
        for k,v in C.items():
            stack+=[k]*v
        return ''.join(sorted([str(x) for x in stack]))
        