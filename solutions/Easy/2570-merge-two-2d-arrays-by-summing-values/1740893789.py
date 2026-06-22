class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)

        for id, v in nums1 + nums2:
            d[id]+=v
        

        return sorted([[k,v] for (k,v) in d.items()])
        