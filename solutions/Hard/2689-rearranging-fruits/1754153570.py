class Solution:
    def minCost(self, nums1: List[int], nums2: List[int]) -> int:

        C=Counter(nums1)
        C2=Counter(nums2)
        C3 = C+C2

        good=all([x%2==0 for x in (C3).values()])
        if not good: return -1
        A= []
        B= []
        for k,v in C3.items():
            t = v//2
            if C[k] > t:
                A+=[k]*(C[k]-t)
            if C2[k] > t:
                B+=[k]*(C2[k]-t)
        if not A: return 0
        A.sort()
        B.sort(reverse=True)
        #editorial for 1 case
        mn = min(min(nums1), min(nums2))
        #we can either take the minimum of a,b or we can use the smallest element to go back and
        return sum([min(min(a,b), 2*mn) for a,b in zip(A,B)])

