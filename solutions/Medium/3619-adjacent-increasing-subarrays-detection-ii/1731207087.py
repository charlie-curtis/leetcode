class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        best = [0]*n
        best[0] = 1
        
        for i in range(1,n):
            cur = 1
            if nums[i] > nums[i-1]:
                cur+=best[i-1]
            best[i] = cur
            
            
        l = 0
        r = n
        
        def check(mid):
            for i in range(n):
                if best[i] >= mid and i+mid < n and best[i+mid] >= mid:
                    return True
            return False
        
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1
        
        #TTTTTTFFFFF
        
        return r