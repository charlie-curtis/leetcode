class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        j = 0
        ans = 0
        cur = 0
        #got this on my own, but used editorial for optimizations (both were still O(N))
        for i,x in enumerate(nums):

            while cur & x != 0:
                cur^=nums[j]
                j+=1
            cur|=x
            ans = max(ans, i-j+1)
        return ans
                

        