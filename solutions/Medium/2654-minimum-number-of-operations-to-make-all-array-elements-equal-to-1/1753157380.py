class Solution:
    def minOperations(self, nums: List[int]) -> int:

        #[2], [2*3], [3], [2*2], [7]


        #how quickly can we get 2 neighbors to be coprime?
        #cost = i-j+1 = 

        n = len(nums)

        #if there is already a 1 in nums, then it can "infect" the non-1 elements once per second
        if 1 in nums:
            return n - nums.count(1)
        
        #if we were to gcd all the numbers together and they still don't equal 1, no solution exists
        if reduce(gcd, nums) != 1:
            return -1
        ans = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i,n):
                g = gcd(g, nums[j])
                if g == 1:

                    #I came up with this equation through modeling the problem. Basically, for each starting element, we find the smallest subarray where gcd(nums[i], nums[i+1],...,nums[j]) == 1. Then, to make that block have atleast one "1", it costs j-i moves. To convert the remaining block, it costs another j-i moves. To convert the non-subarray elements, it costs n-SizeOfWindow moves.
                    can = 2*(j-i) + n-(j-i+1)
                    ans = min(ans, can)
                    break
        return ans

