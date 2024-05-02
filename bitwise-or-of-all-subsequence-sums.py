class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:

        #iterate over all the bits in each number,
        #adding them to the Counter if the bit position is set
        c = Counter()
        for x in nums:
            for i in range(64):
                if x&(1<<i) > 0:
                    c[i]+=1

        ans = 0
        #iterate over the Counter. If the bit position is > 1, then set that bit in the answer
        #also, we can borrow any previously set bits
        for i in range(64):
            if c[i] > 0:
                ans|=(1<<i)
            c[i+1]+= c[i]//2
            
        return ans
