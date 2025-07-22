class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:

        #LCM is < k = expand
        #LCM > k -> subtract

        n = len(nums)
        ans = 0
        for i in range(n):
            l = nums[i]
            j = i
            for j in range(i,n):
                l = lcm(l, nums[j])
                if l == k:
                    ans+=1
                if l > k:
                    break
        return ans

        