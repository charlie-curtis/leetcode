class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:


        c = Counter(barcodes)
        mmax = max(c.values())

        start = -1
        for k,v in c.items():
            if v == mmax:
                start = k
                break
        
        ans = [0]*len(barcodes)

        n = len(barcodes)

        idx = 0
        for i in range(c[start]):
            ans[idx] = start
            idx+=2

        for k,v in c.items():
            if k == start:
                continue
            for i in range(v):
                if idx >= len(ans):
                    idx = 1
                ans[idx] = k
                idx+=2
        return ans