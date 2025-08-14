class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)

        def check(s1,s2):
            i = j = 0
            seen = set()
            while i < m:
                if i in [s1,s2]:
                    i+=1
                    continue
                seen.add(nums2[j] - nums1[i])
                if len(seen) > 1:
                    return float('inf')
                i+=1
                j+=1
            return list(seen)[0]
        
        ans = float('inf')
        for i in range(m):
            for j in range(i+1,m):
                ans = min(ans, check(i,j))
        return ans
                


        