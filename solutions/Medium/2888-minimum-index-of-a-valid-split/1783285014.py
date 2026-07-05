class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        b = 0
        can = -1
        #boyer moore
        for x in nums:
            if b == 0:
                can = x
            if x == can:
                b+=1
            else:
                b-=1

        rcnt = nums.count(can)
        n = len(nums)
        lcnt = 0

        #simulate every splitting index
        for i in range(n-1):
            if nums[i] == can:
                rcnt-=1
                lcnt+=1

            lsize = i+1
            rsize = n - lsize
            if 2*lcnt > lsize and 2*rcnt > rsize:
                return i
            
        return -1
        