class Solution:
    def prevPermOpt1(self, nums: List[int]) -> List[int]:
        n= len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] > nums[i+1]:
                mx=-1
                for j in range(i+1,n):
                    if nums[i] > nums[j]:
                        mx=max(mx,nums[j])
                for j in range(i+1,n):
                    if nums[j]== mx:
                        nums[i],nums[j] = nums[j],nums[i]
                        return nums
        return nums