class Solution:
    def maxLength(self, nums: List[int], k: int) -> int:


        n = len(nums)

        l = 1
        r = max(nums)

        def check(mid):
            cnt = 0
            for x in nums:
                cnt+=x//mid

            return cnt >=k

        #TTTTTFFFFFF
        while l <= r:
            mid = l + (r-l)//2

            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r