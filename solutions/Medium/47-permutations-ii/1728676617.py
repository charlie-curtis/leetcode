class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set([tuple(x) for x in list(permutations(nums))])