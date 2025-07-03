class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:

        j=0
        ssum=0
        n=len(nums)
        best=1e20
        for i in range(n):
            ssum+=nums[i]
            while ssum>=k:
                best=min(best,i-j+1)
                ssum-=nums[j]
                j+=1
        return best if best !=1e20 else 0

        