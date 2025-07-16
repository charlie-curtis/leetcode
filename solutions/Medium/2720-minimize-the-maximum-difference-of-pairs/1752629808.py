class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        nums.sort()
        n = len(nums)


        l = 0
        r = 2*10**9

        def check(mid):
            i = 0
            cnt = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= mid:
                    cnt+=1
                    i+=2
                else:
                    i+=1
            return cnt >= p

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l
        