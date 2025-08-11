class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:

        T = sum(nums)
        D = abs(goal - T)
        return ((D+limit-1)//limit)
        