class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        far = nums[0]
        for i in range(1, n):
            if i > far:
                return False
            far = max(far, nums[i] + i)

        return True
        