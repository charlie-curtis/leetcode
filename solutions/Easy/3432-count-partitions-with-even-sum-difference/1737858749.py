class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        ans = 0
        n = len(nums)
        for i in range(n-1):
            left+=nums[i]
            right-=nums[i]
            if abs(left-right) % 2 == 0:
                ans+=1
        return ans
        