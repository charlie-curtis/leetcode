class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:

        C = Counter(nums)
        mmin = min(nums)
        v = C[mmin]

        for x in C.keys():
            if x % mmin != 0:
                return 1
        
        #we can't do any better than our original smallest number
        return int(ceil(v/2))