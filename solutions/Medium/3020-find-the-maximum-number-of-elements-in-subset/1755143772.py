class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        L = Counter()
        C = Counter(nums)

        for k in sorted(C.keys()):
            if k == 1:
                continue
            L[k] = max(L[k], 1)
            if C[k] > 1 and C[k*k] > 0:
                L[k*k] = L[k] + 1

        mx = 0 if not L else max(L.values()) 
        can = C[1] if C[1]%2 else C[1]-1 #edge case with (1,1,1,1,1,1,1,) etc
        return max(can, mx*2-1)
        

        