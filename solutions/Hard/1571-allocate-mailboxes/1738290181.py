class Solution:
    def minDistance(self, nums: List[int], k: int) -> int:


        nums.sort()
        n = len(nums)

        @cache
        def dp(i, rem):
            if rem < 0:
                return 1e15
            if i == n:
                return 0
            ans = 1e15
            for j in range(i,n):
                tmp = nums[i:j+1]
                m = median(tmp)
                can = sum([abs(a-m) for a in tmp])
                ans = min(ans, can + dp(j+1, rem-1))
            return ans
        return int(dp(0, k))
                
                