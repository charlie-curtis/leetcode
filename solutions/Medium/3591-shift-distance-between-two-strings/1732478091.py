class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], prevCost: List[int]) -> int:

        if s == t:
            return 0

        n = 26
        def forward(a,b):
            a,b = ord(a)-ord('a'), ord(b)-ord('a')
            if a > b:
                b+=26

            cost = 0
            for i in range(a,b):
                cost+=nextCost[i%n]
            return cost

        def backward(a,b):
            a,b = ord(a)-ord('a'), ord(b)-ord('a')
            if a < b:
                a+=26

            cost = 0
            for i in range(b+1,a+1):
                cost+=prevCost[i%n]
            return cost



        ans = 0
        for a,b in zip(s,t):
            ans+= min(forward(a,b), backward(a,b))
        return ans