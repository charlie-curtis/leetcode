class Solution:
    def maximumSwap(self, num: int) -> int:


        num = str(num)
        d = {}

        A = []
        for i,x in enumerate(num):
            A.append(x)
            d[x] = i

        keep = True
        for i,x in enumerate(A):
            if not keep:
                break
            for j in range(9, -1, -1):
                if j > int(x) and str(j) in d and d[str(j)] > i:
                    keep = False
                    A[i], A[d[str(j)]] = A[d[str(j)]], A[i]
                    break

        return int(''.join([str(x) for x in A]))

        