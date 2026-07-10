class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        n = len(s)
        cnts = [[0 for _ in range(26)] for _ in range(n+1)]
        for i,x in enumerate(s):
            for j in range(26):
                cnts[i+1][j] = cnts[i][j]
            v = ord(x) - ord('a')
            cnts[i+1][v]+=1

        def check(start,end, k):
            ssum = 0
            for i in range(26):
                t1 = cnts[end+1][i]
                t2 = cnts[start][i]
                ssum+=((t1-t2) % 2)
            
            if (end-start+1) % 2 == 1:
                #get the midddle character for free
                ssum-=1
            return ssum/2 <= k
        return [check(x,y,z) for x,y,z in queries]