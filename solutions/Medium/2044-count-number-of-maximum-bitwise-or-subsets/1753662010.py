class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        mmax = reduce(lambda x,y: x|y, nums)

        n = len(nums)
        @cache
        def bt(i, can):
            if i == n:
                return 1 if can == mmax else 0

            return bt(i+1, can) + bt(i+1, can|nums[i])

        return bt(0, 0)
