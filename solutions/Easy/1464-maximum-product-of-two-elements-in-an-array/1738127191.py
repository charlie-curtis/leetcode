class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        best = -1e15
        for i in range(n):
            for j in range(i+1, n):
                best = max(best, (nums[i]-1)*(nums[j]-1))
        return best
                
        