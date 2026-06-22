class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ans = 0
        mmax = max(nums)
        while mmax > 0:
            mmax = 0
            odds = 0
            for i,x in enumerate(nums):
                if x % 2 == 1:
                    odds+=1
                    mmax = max(mmax, x-1)
                    nums[i] = (x-1)//2
                else:
                    mmax = max(mmax, x)
                    nums[i] = (x)//2

            ans+=odds
            if mmax > 0:
                ans+=1
        return ans