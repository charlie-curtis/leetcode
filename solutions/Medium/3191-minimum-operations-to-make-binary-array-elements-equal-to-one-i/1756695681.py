class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                for j in range(i, i+3):
                    if j == n:
                        return -1
                    nums[j] = 1 - nums[j]
                ans+=1
        return ans