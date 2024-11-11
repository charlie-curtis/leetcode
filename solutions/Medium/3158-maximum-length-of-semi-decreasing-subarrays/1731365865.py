from sortedcontainers import SortedList
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:


        '''
        d = defaultdict(int)
        ans = 0
        n = len(nums)
        sl = SortedList()
        for i in range(n-1,-1,-1):
            idx = sl.bisect_left(nums[i])-1
            if idx != -1:
                ans = max(ans, d[sl[idx]] - i + 1)
            
            idx = sl.bisect_right(nums[i])
            if idx == 0:
                d[nums[i]] = i
                sl.add(nums[i])
            
        return ans
        '''


        n = len(nums)
        suffix = [0]*n
        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])

        def check(mid):

            for i in range(n-mid+1):
                if nums[i] > suffix[i+mid-1]:
                    return True
            return False

        
        l = 1
        r = n

        #TTTTTFFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        #TTTTFFFFFF
        return r

                