class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        ans = j = 0

        if k in [0,1]:
            return 0

        prod = 1
        for i in range(n):
            prod*=nums[i]

            while prod >= k:
                prod//=nums[j]
                j+=1
            ans+=i-j+1

        return ans
        