class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:

        has_odd = any([x % 2 == 1 for x in nums])

        if has_odd:
            return (2**(len(nums)-1)) % (10**9 + 7)
        
        return 0