class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        mmax = max(nums)
        mmin = min(nums)
        n = len(nums)

        first_mmin = last_mmax = -1
        for i,x in enumerate(nums):
            if x == mmax:
                last_mmax = i
            if first_mmin == -1 and x == mmin:
                first_mmin = i

        
        ans = first_mmin + n-1 - last_mmax
        if first_mmin > last_mmax:
            ans-=1
        return ans
        