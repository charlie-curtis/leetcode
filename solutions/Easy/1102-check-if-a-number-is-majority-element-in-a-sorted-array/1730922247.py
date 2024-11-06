class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        return r-l > len(nums)/2