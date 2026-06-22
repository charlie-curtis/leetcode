class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:


        def check(A):
            n = len(A)

            best = 0
            cur = 0
            for x in A:
                cur = max(x, x+cur)
                best = max(best,cur)
            return best

        a = check(nums)
        b = check([-x for x in nums])
        return max(a,b)
        