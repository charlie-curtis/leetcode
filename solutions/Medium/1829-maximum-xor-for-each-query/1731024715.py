class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        a = reduce(xor, nums)

        ans = []
        for x in reversed(nums):
            t = 0
            for i in range(maximumBit):
                if (1<<i)&a == 0:
                    t+=(1<<i)
            ans.append(t)
            a^=x

        return ans
        