class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        nums.sort()
        j = 0
        ans = 0
        n = len(nums)
        for i in range(n):
            while (nums[i] - nums[j]) > 2*k:
                j+=1

            ans = max(ans, i-j+1)
        return ans
