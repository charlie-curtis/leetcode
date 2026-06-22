class Solution:
    def specialArray(self, nums: List[int]) -> int:


        n = len(nums)
        ans = 0
        for x in range(0,1001):
            cnt = 0
            for i in range(n):
                if nums[i] >= x:
                    cnt+=1
            if cnt == x:
                return x
        return -1
        