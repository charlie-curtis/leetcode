class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:


        C1 = Counter()
        C2 = Counter()

        for x in nums1:
            C1[x**2]+=1
        for x in nums2:
            C2[x**2]+=1

        ans = 0

        n = len(nums1)
        for i in range(n):
            for j in range(i+1,n):
                ans+=C2[nums1[i]*nums1[j]]
            
        n = len(nums2)
        for i in range(n):
            for j in range(i+1,n):
                ans+=C1[nums2[i]*nums2[j]]
        return ans
            
        