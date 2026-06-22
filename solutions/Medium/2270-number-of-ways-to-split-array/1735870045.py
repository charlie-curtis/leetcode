class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        rem, ssum = sum(nums), 0
        ans = 0
        
        for i in range(n-1):
            rem-=nums[i]
            ssum+=nums[i]
            if ssum >= rem:
                ans+=1
                
        return ans

        