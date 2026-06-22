from sortedcontainers import SortedList
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:

        n = len(nums)
        to_left = [0]*n
        to_right = [0]*n

        tmp = SortedList()
        for i in range(n):
            to_left[i] = tmp.bisect_left(nums[i])
            tmp.add(nums[i])

        tmp = SortedList()
        for i in range(n-1, -1, -1):
            to_right[i] = tmp.bisect_left(nums[i])
            tmp.add(nums[i])

        ans = 0
        for i in range(n):
            if to_left[i] >= k and to_right[i] >= k:
                ans+=1
        return ans

        

        