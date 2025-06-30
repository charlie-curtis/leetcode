class Solution:
    def findLHS(self, nums: List[int]) -> int:

        C = Counter(nums)

        best = 0
        for k,v in C.items():
            if k-1 in C:
                best = max(best, C[k] + C[k-1])
        return best

        