class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if k == 0:
            return 0 if nums1 == nums2 else -1

        lower = 0
        upper = 0
        for s, t in zip(nums1,nums2):
            if s == t:
                continue
            d = abs(s-t)
            if d % k:
                return -1
            if s > t:
                lower+=d//k
            else:
                upper+=d//k
        
        if lower == upper:
            return lower
        return -1
            
        