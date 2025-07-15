class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:

        ans = 0
        streak = 1
        n = len(nums)
        for i in range(1,n):
            if 1 - nums[i] == nums[i-1]:
                #streak continues
                streak+=1
            else:
                ans+=streak*(streak+1)//2
                streak = 1
        ans+=streak*(streak+1)//2
        return ans