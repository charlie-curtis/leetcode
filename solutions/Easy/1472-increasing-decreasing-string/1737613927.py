class Solution:
    def sortString(self, s: str) -> str:

        A = [ord(x) - ord('a') for x in s]
        A.sort()


        out = []
        while A:
            prev = -1
            while A:
                idx = bisect_left(A, prev+1)
                if idx == len(A):
                    break
                else:
                    out.append(A.pop(idx))
                    prev = out[-1]
            prev = 1e15
            while A:
                idx = bisect_right(A, prev-1) -1
                if idx == -1:
                    break
                else:
                    out.append(A.pop(idx))
                    prev = out[-1]

        return ''.join([chr(x + ord('a')) for x in out])
            