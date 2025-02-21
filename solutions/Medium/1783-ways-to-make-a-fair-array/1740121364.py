class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        n = len(nums) 
        odds = [nums[i] if i % 2 == 1 else 0 for i in range(n)]
        evens = [nums[i] if i % 2 == 0 else 0 for i in range(n)]

        prefodd = list(accumulate(odds, initial=0))
        prefeven=list(accumulate(evens, initial=0))


        ans = 0
        for i in range(n):
            odd = prefodd[i]
            even = prefeven[i]
            if i != n-1:
                odd+=prefeven[-1] - prefeven[i+1]
                even+=prefodd[-1] - prefodd[i+1]
            if odd==even:
                ans+=1
        return ans
        
        