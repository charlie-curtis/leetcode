class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        out = []
        for i in range(n//2):
            out.append(nums[i])
            out.append(nums[i+n//2])
        return out
        