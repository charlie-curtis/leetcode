class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
        j = ans = 0
        zeros = 0
        for i in range(n):
            if nums[i] == 0:
                zeros+=1
            
            while zeros > k:
                if nums[j] == 0:
                    zeros-=1
                j+=1

            ans = max(ans, i-j+1)
        return ans
            

        