class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        d = {}
        d[0] = -1 

        n = len(nums)
        ssum = ans = 0
        for i in range(n):
            ssum+=nums[i]
            target = ssum - k
            if target in d:
                ans = max(ans, i-d[target])
            
            if ssum not in d:
                d[ssum] = i

        return ans
        