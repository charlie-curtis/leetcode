class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        n = len(nums1)

        C=Counter()
        A = []
        for i in range(n):
            for j in range(n):
                A.append(nums1[i]+nums2[j])
                C[nums3[i]+nums4[j]]+=1

        ans = 0
        for x in A:
            ans+=C[-x]
        return ans

        


        