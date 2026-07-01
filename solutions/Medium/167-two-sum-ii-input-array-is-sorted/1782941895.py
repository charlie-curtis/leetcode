class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        j = n-1
        for i in range(n):
            while nums[i] + nums[j] > target:
                j-=1
            if nums[i] + nums[j] == target:
                return [i+1, j+1]