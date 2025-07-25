class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        
        #editorial. The thing to note here is that it's never advantagous to include an item in your sub array that is going the "wrong direction", but even more than that, within a same-sign group, you need to figure out which ones you can group within a sub array (hint= monotonic stack)


        #mountain processing algorithm. We only actually care about the peak of the mountains

        #1,2,3,4,3,2,1,5,10,9,6,8 (difference array) -> mountains are 4, 10, 8, but we dont have to pay full price

        #4 + 4 + 5 + 2

        nums = [t-x for (t,x) in zip(nums,target)]
        n = len(nums)

        ans = 0
        height = 0
        #print(nums)
        for i in range(n):
            if i == 0 or nums[i] == 0 or ((nums[i] <= 0) != (nums[i-1] <= 0)):
                height = 0
                #print("height change at", i)
            
            if abs(height) < abs(nums[i]):
                ans+=abs(nums[i]) -abs(height)
            height = nums[i]
            #print("height is", height)
        return ans