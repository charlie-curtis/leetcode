class Solution:
    def removeKdigits(self, tmp: str, k: int) -> str:

        #k=2
        #7891
        #7819

        #1131 k = 2
        #11190

        #2223 = k 2
        stack = []
        nums = [int(x) for x in str(tmp)]
        n = len(nums)
        nxt_lower = [n]*n
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                nxt_lower[i] = stack[-1]
            stack.append(i)

        out = []
        for i,x in enumerate(nums):
            if k and (nxt_lower[i]-i) <=k:
                k-=1
                continue
            else:
                out.append(str(x))
        j = 0
        while j < len(out) and out[j] == '0':
            j+=1
        
        res = ''.join(out[j:])
        if not res:
            return "0"
        return res
        