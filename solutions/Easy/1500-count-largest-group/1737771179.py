class Solution:
    def countLargestGroup(self, n: int) -> int:
        C = Counter()
        for i in range(1,n+1):
            x = str(i)
            ssum = sum([int(s) for s in str(x)])
            C[ssum]+=1
        mmax = max(C.values())
        ans = 0
        for k,v in C.items():
            if v == mmax:
                ans+=1
        return ans
        