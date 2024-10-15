class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:

        n = len(nums)
        doubles = Counter()

        ans = 0
        #hash + modding problem
        for i in range(n):
            ans+=doubles[(d - (nums[i] % d))%d]
            for j in range(i):
                ssum = nums[i] + nums[j]
                doubles[ssum%d]+=1
        return ans