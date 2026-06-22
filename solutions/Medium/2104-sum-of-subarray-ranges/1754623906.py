class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        n = len(nums)

        ans = 0
        for i in range(n):
            small = large = nums[i]
            for j in range(i,n):
                small = min(small, nums[j])
                large = max(large, nums[j])
                ans+=abs(large-small)
        return ans



        