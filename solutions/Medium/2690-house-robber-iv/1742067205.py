class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        n = len(nums)

        v = sorted(set(nums))
        l = 0
        r = len(v)-1

        def check(mid):

            i = 0
            n = len(nums)
            rem = k
            while i < n:
                if nums[i] <= mid:
                    rem-=1
                    i+=2
                else:
                    i+=1
                if rem == 0:
                    return True
            return False
        #FFFFFTTTTTT
        while l <= r:
            mid = l + (r-l)//2
            if check(v[mid]):
                r = mid - 1
            else:
                l = mid + 1
        
        return v[l]