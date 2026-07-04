class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)
        #compute initial state
        init = sum([i*nums[i] for i in range(n)]) 
        ssum = sum(nums)

        #work off deltas - O(N)
        ans = init
        for i in range(1,n):
            #the idea here is that every step we move to the right, we move 1 step closer to all values so each value would individually decrease by nums[i] for all i except i-1 (which was already 0 in the answer). for i-1, it would change it's weight from 0 to nums[i-1]*(n-1)
            init = init - ssum + nums[i-1] + nums[i-1]*(n-1)
            ans = max(ans, init)
        return ans
        