# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):

        A = [[i, rand7()] for i in range(1,11)]

        while len(A) > 1:
            mx = -1
            tmp = []
            for i,v in A:
                if v > mx:
                    tmp = [i]
                    mx = v
                elif v == mx:
                    tmp.append(i)
            A = tmp
            if len(A) == 1:
                return A[0]
            A = [[x,rand7()] for x in A]