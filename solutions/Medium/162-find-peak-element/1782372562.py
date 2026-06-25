class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n=len(nums)
        l,r= 0, n-1
        
        def check(i):
            prev = nums[i-1] if i > 0 else -10**10
            fwd = nums[i+1] if i+1 != n else -10**10
            if max(prev, fwd) < nums[i]:
                return 0
            return -1 if prev > fwd else 1
            
        
        while (l <= r):
            mid = l + (r-l)//2
            res = check(mid)
            if res == 0:
                return mid
            if res == -1:
                r = mid - 1
            else:
                l = mid + 1
                
        return -10
            
        