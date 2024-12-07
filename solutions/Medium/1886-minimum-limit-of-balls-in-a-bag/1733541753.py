class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        mmax = max(nums)
        l = 1
        r = mmax-1

        def check(k):

            t = 0
            for x in nums:
                t+= (ceil(x/k)-1)
            return t <= maxOperations


        #FFTTTTTT
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        