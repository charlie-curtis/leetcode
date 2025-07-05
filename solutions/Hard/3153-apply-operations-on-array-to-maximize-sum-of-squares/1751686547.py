class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:


        #1001 = 9
        #1000 = 8
        #0001 = 1

        #81 vs 64 + 1 = 65

        #1. What is the strategy? I know we want
        #to transfer bits, and it's better to dump
        #all your bits in a single number
        #than to try to evenly spread out the bits
        #across k numbers

        #is it best to always choose the k biggest
        #numbers and go from there?

        #111
        #011
        #010

        #so let's try this: choose the K biggest numbers. anything that isn't chosen is a "free" number
        #hash the bits and greedily redistribute them over the largest numbers first

        #not 100% sure if that works, but makes sense to me


        n = len(nums)
        free = Counter()
        for x in nums:
            for i in range(32):
                if x&(1<<i):
                    free[i]+=1
        
        ans = 0
        MOD = 10**9 + 7
        for _ in range(k):
            cur = 0
            for i in range(32):
                if free[i]:
                    free[i]-=1
                    cur|=(1<<i)
            ans+=cur*cur
            ans%=MOD
        return ans