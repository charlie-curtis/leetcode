class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()
        l = 0
        r = len(nums)-1

        ans = -1
        while l < r:
            ssum = nums[l] + nums[r]
            if ssum < k:
                ans = max(ans, ssum)
                l+=1
            else:
                r-=1
        return ans

        