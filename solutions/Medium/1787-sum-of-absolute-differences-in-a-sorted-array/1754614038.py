class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        T = sum(nums)
        seen = 0

        A = sorted([[nums[i],i] for i in range(len(nums))])

        out = [0]*n
        for i,(x,j) in enumerate(A):
            T-=x
            before = i*x - seen
            after = T - (n-1-i)*x

            out[j] = before+after
            seen+=x
        return out
