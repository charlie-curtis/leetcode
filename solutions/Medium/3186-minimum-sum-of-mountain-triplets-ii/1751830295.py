class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        n = len(nums)
        INF = 10**9
        left = [-1]*n
        small = INF
        for i,x in enumerate(nums):
            if small < x:
                left[i] = small
            small = min(small, x)

        
        small = INF
        ans = INF 
        for i in range(n-1, -1, -1):
            x = nums[i]
            if x > small and left[i] != -1:
                ans = min(ans, small + left[i] + x)
            small = min(small, x)
        return ans if ans != INF else -1
