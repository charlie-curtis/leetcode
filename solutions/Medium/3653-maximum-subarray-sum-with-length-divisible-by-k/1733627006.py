class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        d = {}

        ssum = 0
        ans = -1e15 
        d[0] = 0
        for i in range(n):
            x = nums[i]
            ssum+=x
            rem = (i+1)%k
            if rem in d:
                ans = max(ans, ssum - d[rem])
                d[rem] = min(d[rem], ssum)
            else:
                d[rem] = ssum
        return ans