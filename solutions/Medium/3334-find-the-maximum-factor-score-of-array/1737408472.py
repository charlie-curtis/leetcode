class Solution:
    def maxScore(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]*nums[0]

        best = 0

        gcdf = lambda x,y: gcd(x,y)
        lcmf = lambda x,y: lcm(x,y)
        g = reduce(gcdf, nums)
        p = reduce(lcmf, nums)
        best = g*p
        n = len(nums)
        for i in range(n):
            A = nums[:i] + nums[i+1:]
            best = max(best, reduce(gcdf, A)*reduce(lcmf, A))
        return best