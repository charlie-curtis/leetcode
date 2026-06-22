class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        C = Counter(nums)
        high = -1
        for k,v in C.items():
            if v == 1 and k > high:
                high = k
        return high