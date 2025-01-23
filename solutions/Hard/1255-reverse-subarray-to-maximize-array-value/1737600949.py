class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:

        #tricky case work problem that i had to look at the solutions for
        #I was over it
        mmin = 1e15
        n = len(nums)
        A = list(zip(nums, nums[1:]))
        ans = sum([abs(a-b) for a,b in A])
        def score(nums):
            best = 0
            small = 1e15 
            large = -1e15 
            for i in range(n-1):
                small = min(small, max(nums[i], nums[i+1]))
                large = max(large, min(nums[i], nums[i+1]))
            best = max(best, 2*(large-small))
            return best

        def pref(nums):
            best = 0
            for i in range(1,n):
                old = abs(nums[i] - nums[i-1])
                new = abs(nums[0] - nums[i])
                best = max(best, new -old)
            print(best)
            return best

        


        a, b = score(nums), score(nums[::-1])
        c, d = pref(nums), pref(nums[::-1])

        print(ans)
        return ans + max(a,b,c ,d)
