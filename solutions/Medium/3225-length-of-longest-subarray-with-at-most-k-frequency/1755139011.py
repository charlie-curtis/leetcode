class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        ans = j = 0
        C = Counter()
        n = len(nums)
        for i in range(n):
            C[nums[i]]+=1

            while C[nums[i]] > k:
                C[nums[j]]-=1
                j+=1
            ans = max(ans, i-j+1)
        return ans
        