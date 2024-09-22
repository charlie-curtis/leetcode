class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        '''
        full = [x for x in range(0, len(nums)+1)]
        return reduce(xor, nums + full)
        '''

        n = len(nums)
        for i in range(n):
            while nums[i] != i:
                #print(nums, i)
                if nums[i] == n:
                    #can't place it, so ignore it
                    break
                #nums[1], nums[0] = nums[0], nums[1]
                #print("bout to swap", nums[i], i, "with values", nums[i], nums[nums[i]])
                #print(nums[i])
                val = nums[i]
                nums[i], nums[val] = nums[val], nums[i]
        
        for i,x in enumerate(nums):
            if i != x:
                return i
        return n