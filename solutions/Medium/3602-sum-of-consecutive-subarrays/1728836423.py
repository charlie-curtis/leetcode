class Solution:
    def getSum(self, nums: List[int]) -> int:

        n = len(nums)
        MOD = 10**9 + 7


        sums = [0,0]
        lengths = [0,0]
        ans = 0
        #this problem is tricky and the math is non-intuitive. looked at the solutions
        #the idea is we need to keep a track of the previous sums and add that everytime we extend
        #our subarray
        for i in range(n):
            if i == 0 or (nums[i] - nums[i-1] != 1):
                sums[0] = 0
                lengths[0] = 0
            if i == 0 or (nums[i] - nums[i-1] != -1):
                sums[1] = 0
                lengths[1] = 0
            
            lengths[0]+=1
            lengths[1]+=1
            sums = [sums[0] + lengths[0]*nums[i], sums[1] + lengths[1]*nums[i]]
            ans+= sum(sums) % MOD
        return (ans - sum(nums)) % MOD