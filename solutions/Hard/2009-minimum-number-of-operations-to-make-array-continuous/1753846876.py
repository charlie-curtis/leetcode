class Solution:
    def minOperations(self, nums: List[int]) -> int:

        #all nums must be unique
        #high - low must be n-1
        n = len(nums)

        #iterate over all nums
        #keep a sorted list
        nums.sort()
        ans = 10**9 
        A = sorted(set(nums))
        for low in A:
            #low = nums[i]
            #high = n-1+low
            high = n-1+low
            l,r = bisect_left(A, low), bisect_right(A,high)-1
            good = r-l+1
            ans = min(ans, n-good)
        return ans

            

        