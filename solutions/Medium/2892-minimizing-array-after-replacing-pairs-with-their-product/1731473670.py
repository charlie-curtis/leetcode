class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:


        n = len(nums)
        if n == 1:
            return 1
        if 0 in nums:
            return 1
        cur = 1
        ans = 0
        for i in range(n):
            if cur*nums[i] > k:
                ans+=1
                cur = 1
            cur*=nums[i]

        return ans+1
        