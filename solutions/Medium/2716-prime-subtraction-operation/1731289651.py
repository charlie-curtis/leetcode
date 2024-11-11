class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        cans = [True]*1001
        cans[0] = False

        for i in range(2,1001):
            if i*i > 1001:
                break
            if cans[i]:
                k = 2
                while i*k <= 1000:
                    cans[i*k] = False
                    k+=1

        primes = [i for i in range(2,1001) if cans[i]]

        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] >= nums[i+1]:
                #need to find the smallest prime that is gte diff
                diff = nums[i] - nums[i+1] + 1
                idx = bisect_left(primes, diff)
                if idx == len(primes) or primes[idx] >= nums[i]:
                    return False
                nums[i]-=primes[idx]
        return True