class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:


        def check(A):
            n = len(A)
            cur = 1
            best = 1
            for i in range(1,n):
                if A[i] > A[i-1]:
                    cur+=1
                else:
                    cur = 1
                best = max(best, cur)
            return best


        return max(check(nums), check(nums[::-1]))

        