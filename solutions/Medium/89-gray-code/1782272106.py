class Solution:
    def grayCode(self, n: int) -> List[int]:

        #00 -> 01, 10
        #01 -> 11, 00
        #10 -> 00, 11
        #11 -> 10, 01

        #000 -> 100, 010, 001 X
        #001 -> 101, 011, 000 X
        #010 -> 011, 110, 000 X
        #011 -> 111, 001, 010 X
        #100 -> 110, 101, 000 X
        #101 -> 001, 111, 100 X
        #110 -> 010, 100, 111 X
        #111 -> 011, 101, 110 X


        #for each number, keep a list of which "nodes" it is connected to. Just traverse those til you've processed all of them

        seen = set({0})
        out = [0]
        while len(out) < 2**n:
            for i in range(n):
                Y = out[-1]^(1<<i)
                if Y not in seen:
                    seen.add(Y)
                    out.append(Y)
                    break
        return out
                