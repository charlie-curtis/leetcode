class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:


        t = sum(nums) % p
        if t == 0:
            return 0

        d = {}
        d[0] = -1

        ssum = 0
        ans = 1e15
        for i,x in enumerate(nums):
            ssum+=x
            ssum%=p
            if (ssum - t)%p in d:
                ans = min(ans, i - d[(ssum-t)%p])

            d[ssum] = i

        if ans == 1e15 or ans == len(nums):
            return -1
        return ans
        