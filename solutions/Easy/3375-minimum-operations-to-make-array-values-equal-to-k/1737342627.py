class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if min(nums) < k:
            return -1


        ans = len(set(nums))
        if k in nums:
            ans-=1
        return ans