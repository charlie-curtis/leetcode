class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        ans = 0
        n = len(nums)
        for i,x in enumerate(nums):
            g = x
            for j in range(i,n):
                y = nums[j]
                g = gcd(g, y)
                if g < k:
                    break
                if g == k:
                    ans+=1
        return ans