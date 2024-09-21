class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #m is the size of nums1 of "good" elements
        #n is the size of nums2 of "good" elements. It has no extra space

        offset = 1
        for i in range(m-1, -1, -1):
            nums1[-offset] = nums1[i]
            offset+=1
        
        p1 = n
        p2 = 0
        
        for i in range(m+n):
            a = 1e12 if p1 >= n+m else nums1[p1]
            b = 1e12 if p2 >= n else nums2[p2]
            val = 0
            if a <= b:
                nums1[i] = nums1[p1]
                p1+=1
            else:
                nums1[i] = nums2[p2]
                p2+=1