class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:


        d = defaultdict(int)
        for start,end in queries:
            d[start]+=1
            d[end+1]-=1


        cur = 0
        n = len(nums)
        for i in range(n):
            cur+=d[i]
            if nums[i] > cur:
                return False
        return True
        