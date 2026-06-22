class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        last = -1e15
        for i,x in enumerate(nums):
            if x == 0:
                continue
            if i - last-1< k:
                return False
            last = i
        return True
        