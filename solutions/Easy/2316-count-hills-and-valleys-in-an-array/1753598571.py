class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=len(nums)
        nums = [nums[0]]+ [nums[i] for i in range(1,n) if nums[i] != nums[i-1]]
        n=len(nums)

        ans=0

        for i in range(1,n-1):
            a=nums[i-1]>nums[i]
            b=nums[i]<nums[i+1]
            ans+=int(a == b)
        return ans
            