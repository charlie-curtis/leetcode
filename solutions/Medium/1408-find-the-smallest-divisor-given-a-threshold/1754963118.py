class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:


        l = 1
        r = 10**6 + 1

        def check(mid):
            return sum([(x+mid-1)//mid for x in nums]) <= threshold
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
        