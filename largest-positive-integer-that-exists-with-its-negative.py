class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        c = Counter(nums)
        a = [x for x in c if c[-x]>0]
        return max(a) if a else -1
        
