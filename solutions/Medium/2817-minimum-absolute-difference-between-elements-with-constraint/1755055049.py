class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        ss = SortedSet()
        n = len(nums)

        ans = 10**9
        for i in range(x,n):
            ss.add(nums[i-x])
            lower_idx = ss.bisect_right(nums[i])-1
            greater_idx = ss.bisect_left(nums[i])
            if lower_idx != -1:
                ans = min(ans, nums[i] - ss[lower_idx])
            if greater_idx != len(ss):
                ans = min(ans, ss[greater_idx] - nums[i])
        return ans


        