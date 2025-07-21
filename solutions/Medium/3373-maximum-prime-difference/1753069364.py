class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        mx = max(nums)
        primes = [True]*(mx+1)
        primes[0] = primes[1] = False

        i = 2
        n = len(nums)
        while i*i <= mx:
            if primes[i]:
                j = 2
                while j*i <= mx:
                    primes[j*i] = False
                    j+=1
            i+=(1 if i == 2 else 2)
        
        first = last = -1 
        for i,x in enumerate(nums):
            if not primes[x]:
                continue
            last = i
            if first == -1:
                first = i
        return last - first
        