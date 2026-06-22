class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        base = nums.count(k)
        best = base

        def check(x):
            small = 0
            xC = 0
            kC = 0
            ans = 0
            for y in nums:
                if y == k:
                    kC+=1
                elif y == x:
                    xC+=1

                delta = xC - kC
                ans = max(ans, (delta-small))
                small = min(small, delta)
            return ans + base

        for i in range(1,51):
            if i == k:
                continue
            best = max(best,check(i))
            
        return best
        