class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        C = Counter(nums1) & Counter(nums2)

        out = []
        for k,v in C.items():
            out+= [k]*v
        return out
        