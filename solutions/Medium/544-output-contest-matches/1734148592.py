class Solution:
    def findContestMatch(self, n: int) -> str:

        def bt(cur):
            if len(cur) == 1:
                return cur[0]
            
            n = len(cur)
            pairs = []
            for i in range(n//2):
                pairs.append("(" + cur[i] + "," + cur[n-1-i] + ")")
            return bt(pairs)

        return bt([str(x) for x in range(1,n+1)])