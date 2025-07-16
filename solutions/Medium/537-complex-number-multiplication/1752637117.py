class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        def parse(num):
            k = num.find('+')
            return [int(num[:k]), int(num[k+1:-1])]

        
        out = [0,0]
        T,S = parse(num1), parse(num2)
        out[0]+= T[0]*S[0]
        out[1]+= T[0]*S[1]
        out[1]+= T[1]*S[0]
        out[0]-= T[1]*S[1]

        return str(out[0])+ "+" + str(out[1]) + "i"
