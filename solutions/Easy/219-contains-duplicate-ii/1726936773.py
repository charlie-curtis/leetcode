class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        lastSeen = {}
        for i,x in enumerate(nums):
            if x in lastSeen and i - lastSeen[x] <= k:
                return True
            lastSeen[x] = i
        return False
        