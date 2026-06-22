class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        def check(o):
            cnt = 0
            for i in range(n):
                a = nums1[(i+o)%n]
                b = nums2[i]
                cnt+=1 if a==b else 0
            return cnt
        
        return max([check(i) for i  in range(n)])
        