class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        def check(sz):
            n = len(nums)
            j = 0
            ssum = 0
            can = 1e15
            for i in range(n):
                ssum+=nums[i]

                if i-j+1 > sz:
                    ssum-=nums[j]
                    j+=1

                if i-j+1 == sz and ssum > 0:
                    can = min(can, ssum)

            return can

        can = 1e15
        for i in range(l, r+1):
            can = min(can, check(i))

        return can if can != 1e15 else -1
                
            
        