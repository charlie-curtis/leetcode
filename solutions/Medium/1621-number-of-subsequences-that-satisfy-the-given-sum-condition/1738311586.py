class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        MOD = 10**9 + 7
        ans=0
        for i,x in enumerate(nums):
            j = bisect_right(nums, target-x)
            if i >= j:
                continue
            ans+=2**(j-i-1)
            ans%=MOD
        return ans

            #3
            #3,5
            #3,6
            #3,7
            #3,5,6
            #3,5,7
            #3,6,7
            #3,5,6,7
        