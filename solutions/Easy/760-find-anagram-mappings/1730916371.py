class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = defaultdict(list)
        n = len(nums1)

        for i,x in enumerate(nums2):
            d[x].append(i)

        ans = [0]*n

        for i,x in enumerate(nums1):
            ans[i] = d[x].pop()
        return ans
        