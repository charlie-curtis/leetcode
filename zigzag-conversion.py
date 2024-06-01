#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        A = [[] for _ in range(numRows)]
        ptr = 0
        isIncreasing = True
        for x in s:

            A[ptr].append(x)
            ptr+= 1 if isIncreasing else -1
            if ptr == numRows:
                isIncreasing = False
                ptr-=2
            elif ptr == -1:
                isIncreasing = True
                ptr = 1


        ans = []
        for i in range(numRows):
            ans+=A[i]
        return ''.join(ans)
