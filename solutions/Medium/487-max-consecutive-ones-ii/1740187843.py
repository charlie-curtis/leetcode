class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)
        j = ans = 0
        used = 0

        for i in range(n):
            if nums[i] == 0:
                used+=1
            while used > 1:
                if nums[j] == 0:
                    used-=1
                j+=1
            
            ans = max(ans, i-j+1)
        return ans
