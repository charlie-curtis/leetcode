class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:


        l = 0
        r = 10**9

        def check(mid):
            carry = 0
            n = len(nums)
            for i in range(n-1, 0, -1):
                a = nums[i] + carry
                if a <= mid:
                    carry = 0
                else:
                    carry = a - mid
            
            return nums[0] + carry <= mid


        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l
        