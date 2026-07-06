class Solution:
    def numMovesStonesII(self, nums: List[int]) -> List[int]:

        #this problem roasted me. I had a hard time visualizing the scenarios

        nums.sort()
        zeros = sum([y-x-1 for x,y in zip(nums, nums[1:])])

        #for max moves, we can only choose one of the gaps near the endpoints, but then after that, we can fill all the gaps
        #so compare the gaps at the endpoints
        high = zeros - min(nums[-1] - nums[-2] -1, nums[1] - nums[0] -1)

        #for min moves, we know that we will need a consecutive range of n numbers, so let's look at ranges of size n and figure out how many numbers are already in a given range

        #there is one edge case - provided in the example input - you cannot move the right edge and still ahve it remain the right edge.

        #1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,1,0,1

        low = 10**9
        j = 0
        n = len(nums)
        for i in range(n-1):
            target = nums[i] + n - 1
            while j < n and nums[j] <= target:
                j+=1
            #ones in range
            ones = j-i
            cost = n - ones
            low = min(low, cost)

        if low == 1:
            #handle silly edge case like 3,4,5,6,10
            C = Counter([y-x for x,y in zip(nums, nums[1:])])
            if n > 3 and nums[1] - nums[0] > 2 or nums[-1] - nums[-2] > 2 and C[1] == n-2:
                low+=1


        return [low, high]