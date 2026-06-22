class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        ss = SortedSet(nums1)
        T = sum(abs(x-y) for (x,y) in zip(nums1,nums2))

        ans=T
        for x,y in zip(nums1,nums2):

            lower_idx = ss.bisect_right(y)-1
            if lower_idx != -1:
                can = T - abs(x - y) + abs(y - ss[lower_idx])
                ans=min(ans,can)
            upper_idx = ss.bisect_left(y)
            if upper_idx != len(ss):
                can = T - abs(x-y) + abs(y-ss[upper_idx])
                ans=min(ans,can)
        return ans % (10**9 +7)
        