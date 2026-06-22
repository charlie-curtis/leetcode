class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:


        nums.sort(reverse=True)

        n = len(nums)

        ssum = sum(nums[:k])
        if ssum % 2 == 0:
            return ssum

        
        #if the sum is odd, that means we have an odd number of odds
        #A. remove an odd, replace with an even
        #B. remove an even, replace with an odd

        small_used = [1e15]*2
        for i in range(k):
            idx = nums[i]%2
            small_used[idx] = min(small_used[idx], nums[i])

        large_unused = [-1]*2
        for i in range(k,n):
            idx = nums[i] % 2
            large_unused[idx] = max(large_unused[idx], nums[i])

        a = -1
        for i in range(2):
            small, large = small_used[(i+1)%2], large_unused[i%2]
            if small == 1e15 or large == -1:
                continue
            a = max(a, ssum+large-small)
        
        return a
