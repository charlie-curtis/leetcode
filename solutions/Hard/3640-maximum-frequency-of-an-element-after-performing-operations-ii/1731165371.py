class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        nums.sort()
        n = len(nums)
        ans = 1
        C = Counter(nums)
        
        #with this method, assume we can anchor at x and bring everything to us
        def check_with_dupes(x):
            lower = bisect_left(nums, x-k)
            higher = bisect_right(nums,x+k)-1
            can = higher-lower+1
            ops_used = can - C[x]
            if ops_used > numOperations:
                can = C[x] + numOperations
            

            return can
        
        #with this method, assume all the windows in the range would have to move
        def check(x):
            lower = bisect_left(nums,x)
            higher = bisect_right(nums, x + 2*k)-1
            can = higher - lower + 1
            return min(can, numOperations)
            
        
        for x in set(nums):
            a, b = check_with_dupes(x), check(x)
            ans = max(ans, max(a,b))
        return ans