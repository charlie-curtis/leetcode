class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:


        n = len(nums)

        def countMissing(idx):
            v = nums[idx]
            small = nums[0]
            expected = v-small+1
            actual = idx+1
            missing = expected-actual
            return missing

        def check(mid):
            missing = countMissing(mid)
            return missing >= k


        l = 0
        r = n-1

        #FFFFTTTTTT
        #True = there are k or more values
        #missing to the left

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        if l == n:
            missing = countMissing(n-1)
            rem = k - missing
            return nums[-1] + rem

        before_missing = countMissing(l-1)
        rem = k-before_missing
        return nums[l-1] + rem