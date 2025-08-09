class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        def good(nums, lives):
            n = len(nums)
            for i in range(1,n):
                if nums[i-1] > nums[i]:
                    if not lives: return False
                    return any([
                        good(nums[:i] + nums[i+1:], 0),
                        good(nums[:i-1] + nums[i:], 0)
                    ])
            return True

        return good(nums, 1)
        