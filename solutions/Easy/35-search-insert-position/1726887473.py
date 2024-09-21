class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #return bisect.bisect_left(nums, target)

        l = 0
        r = len(nums) -1
        #1 3 5 7 8 11 15 17
        #FFFFFF TTTTTTT
        #nums[mid] >= target ?
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid -1
            else:
                l = mid + 1
        return l

        