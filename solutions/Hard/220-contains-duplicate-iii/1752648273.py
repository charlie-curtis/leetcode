class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        sl=SortedList()
        n=len(nums)
        j=0
        for i in range(n):
            x=nums[i]
            up=sl.bisect_left(x)
            low=sl.bisect_left(x)-1
            if len(sl) > up and sl[up] - x <= valueDiff:
                return True
            if low >= 0 and x - sl[low] <= valueDiff:
                return True
            sl.add(x)
            if i >= indexDiff:
                sl.remove(nums[i-indexDiff])
        return False
            
        