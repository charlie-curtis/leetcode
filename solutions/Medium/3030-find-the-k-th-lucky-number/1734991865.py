class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        q = deque(['4', '7'])


        #4, 7
        #44, 47, 74, 777
        #444, 447, 474, 477, 744, 747, 774, 777

        #100 - 1 -> 011
        #"find the 4th 3 digit number" -> oh but its 0 indexed
        #4 -> 

        #what if k == 7?
        #find the 1st

        #2 in binary is 10

        #log2(k) = # of digits
        res = int(math.log(k,2))
        print(res)
        #1111

        #each time, it grows by 2x
        k-=1
        digits = 1
        multi = 2
        while k - multi >= 0:
            k-=multi
            multi*=2
            digits+=1

        out = ""
        for x in bin(k)[2:]:
            if x == '1':
                out+='7'
            else:
                out+='4'
        while len(out) < digits:
            out = '4' + out
        return out
        