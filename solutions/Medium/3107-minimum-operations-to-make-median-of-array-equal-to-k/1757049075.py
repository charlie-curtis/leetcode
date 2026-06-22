class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:


        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n//2-1, -1, -1):
            if nums[i] > k:
                ans+=nums[i] - k
                nums[i] = k

        if nums[n//2] != k:
            ans+=abs(nums[n//2] - k)
        
        for i in range(n//2+1, n, 1):
            if nums[i] < k:
                ans+=k - nums[i]
                nums[i] = k
        return ans
        