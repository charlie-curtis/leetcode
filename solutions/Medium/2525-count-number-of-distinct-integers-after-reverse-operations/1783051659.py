class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:


        def rev(x):
            out = 0
            while x > 0:
                out = out*10 + x % 10
                x = x // 10
            return out

        sset = set(nums)
        for x in nums:
            sset.add(rev(x))
        return len(sset)