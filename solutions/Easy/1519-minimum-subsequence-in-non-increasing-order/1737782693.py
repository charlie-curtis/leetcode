class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        left = 0
        right = sum(nums)
        used = []
        for x in nums:
            used.append(x)
            left+=x
            right-=x
            if left > right:
                return used
            
        