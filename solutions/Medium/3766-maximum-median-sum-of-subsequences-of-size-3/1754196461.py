class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:

        nums = deque(sorted(nums)[::-1])

        ans = 0
        while nums:
            nums.popleft()
            ans+=nums.popleft()
            nums.pop()
        return ans
        
        