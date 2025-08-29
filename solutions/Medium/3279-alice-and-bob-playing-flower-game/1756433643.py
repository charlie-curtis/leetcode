class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        A = [n//2 + n%2, n//2]
        B = [m//2 + m%2, m//2]

        return A[0]*B[1] + B[0]*A[1]

        #1 2 3
        #1 2

        #how many ways are there to create odd numbers
        #even + odd
        #so an even from stack 1
        #combined with an odd from stack 2
        