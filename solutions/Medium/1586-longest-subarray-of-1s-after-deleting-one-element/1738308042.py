class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        A = []
        for c, li in groupby(nums):
            A.append([c, len(list(li))])

        best = 0
        n = len(A)
        for i,(c,l) in enumerate(A):
            if c == 0:
                base = 0
                behind = 0 if i-1 < 0 else A[i-1][1]
                forward = 0 if i+1 >= n else A[i+1][1]
                if l == 1:
                    best = max(best, base + behind+forward)
                else:
                    best = max(best, base + max(behind,forward))
            else:
                best = max(best, l if len(A) > 1 else l-1)
        return best
        
        