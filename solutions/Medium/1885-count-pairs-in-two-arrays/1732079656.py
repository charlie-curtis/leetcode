from sortedcontainers import SortedList
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:

        sl = []
        for a,b in zip(nums1, nums2):
            sl.append(a-b)
        sl.sort()
        ans = 0
        n = len(nums1)
        for a,b in zip(nums1, nums2):
            d = a-b
            #so if my diff is -4, then i'd be looking for +5
            #or if my  diff is 1, so i can look for -d + 1 (aka 0)
            lookingFor = -d + 1

            idx = bisect_left(sl, lookingFor)
            ans+=n-idx
            if d > 0:
                #we are subtracting 1 because we don't want to count ourselves
                ans-=1


        return ans//2 #we would have double counted all the pairs

        