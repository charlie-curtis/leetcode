class Solution:
    def orArray(self, nums: List[int]) -> List[int]:


        n = len(nums)
        out = []
        for i in range(n-1):
            out.append(nums[i] | nums[i+1])
        return out
        