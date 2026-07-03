class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(nums)
        prev = -1
        ans = 1

        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                if prev != -1:
                    ans*=(prev - i)
                    ans%=MOD
                prev = i
        return ans if prev != -1 else 0