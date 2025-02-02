class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        out = []
        cur = []
        for x in nums:
            if x == 0:
                if cur:
                    out.append(cur.copy())
                    cur = []
            else:
                cur.append(x)
        if cur:
            out.append(cur.copy())

        def check(A):
            n = len(A)
            last_neg = -1
            negcnt = 0

            ans = 0
            for i,x in enumerate(A):
                if x < 0:
                    negcnt+=1
                    if last_neg == -1:
                        last_neg = i

                if negcnt%2 == 0:
                    ans = max(ans, i+1)
                elif last_neg != -1:
                    ans = max(ans, i-last_neg)
            return ans




        ans = 0
        for x in out:
            #print(x)
            ans = max(ans, check(x))
        return ans
                    
                

                