class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        '''
        l = 0
        ans = 0
        while l < n-1:
            d = nums[l+1] - nums[l]
            r = l+1
            while r < n and (nums[r]  - nums[r-1] == d):
                r+=1
            if r-l+1 >= 3:
                m = r-l+1-3
                ans+=m*(m+1)//2
            l = r-1
        return ans
        '''

        A = [(x-y) for (x,y) in zip(nums, nums[1:])]
        ans = 0
        for _, g in groupby(A):
            m = len(list(g)) + 1
            for x in range(m, 2, -1):
                ans+=m-x+1
        return ans
