class Solution:
    def countAndSay(self, n: int) -> str:


        cur = "1"

        for _ in range(2,n+1):
            tmp = ""
            for c,g in groupby(cur):
                v = str(len(list(g)))
                addin = v + c
                tmp+=addin
            cur = tmp
        return cur
        