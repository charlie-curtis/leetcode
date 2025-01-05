class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            p = nums[i]
            g = nums[i]
            l = nums[i]
            for j in range(i+1,n):
                p*=nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if p == g*l:
                    ans = max(ans, j-i+1)
        return ans
        