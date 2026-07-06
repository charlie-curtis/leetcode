class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        #direct simulation
        n = len(nums)

        best = sum(nums)
        price = 0
        for i in range(n-1):
            hold = nums[n-1]
            price+=x
            for j in range(n-1,0,-1):
                nums[j] = min(nums[j-1], nums[j])
            nums[0] = min(hold, nums[0])
            best = min(best, price + sum(nums))


        return best
        