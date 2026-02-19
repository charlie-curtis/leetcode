class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        m,n = len(num1),len(num2)

        out = [0]*(m*n+1)
        for i in range(n-1, -1, -1):
            carry = 0
            offset = n-1-i
            for j in range(m-1,-1,-1):
                x,y = int(num1[j]), int(num2[i])
                IDX = m-1-j+offset
                out[IDX]+= x*y + carry
                carry = out[IDX] // 10
                out[IDX]%=10
            if carry:
                out[m+offset]+=carry
        
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        return "".join([str(x) for x in out])[::-1]


        