class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        d = {}
        for i,x in enumerate(nums):
            d[x] = i
        
        for f,t in operations:
            idx = d[f]
            nums[idx] = t
            del d[f]
            d[t] = idx
        return nums
        