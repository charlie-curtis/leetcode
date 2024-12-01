class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:

        C = Counter(nums)
        ssum = sum(nums)
        ans = -1e15
        for x in nums:
            can = ssum - x
            diff = can - x
            if x != diff and C[diff] > 0 or (x==diff and C[diff] > 1):
                ans = max(ans, diff)
        return ans
            
        