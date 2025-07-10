class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def check(nums):
            negs = [i for i in range(n) if nums[i] == -1]
            if len(negs) == 0:
                return True
            if len(negs) % 2 == 1:
                return False
            cost = 0
            for i in range(0,len(negs), 2):
                cost+=negs[i+1] - negs[i]
            return cost <= k


        


        if check(nums):
            return True

        nums = [x*-1 for x in nums]
        return check(nums)
        

        