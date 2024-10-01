class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        C = Counter(nums)

        cur = 0
        for i in range(3):
            for v in range(C[i]):
                nums[cur] = i
                cur+=1
        