class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        n = len(nums)
        ans  = 0
        for i in range(n):
            j = max(0, i - nums[i])
            ssum = 0
            for k in range(j, i+1):
                ssum+=nums[k]
            ans+=ssum
        return ans
                
        