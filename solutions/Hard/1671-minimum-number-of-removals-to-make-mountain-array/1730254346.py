class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:


        def compute(A):
            n = len(A)
            dp = [0]*n
            LIS = []
            for i,x in enumerate(A):
                idx = bisect_left(LIS, x)
                dp[i] = i - idx
                if idx == len(LIS):
                    LIS.append(x)
                else:
                    LIS[idx] = x
            return dp



        dp_left = compute(nums)
        dp_right = compute(nums[::-1])[::-1]
        #print(dp_left)
        #print(dp_right)

        #print(dp_left)
        #print(dp_right)
        best = 1e15
        n = len(nums)
        for i in range(1,n-1):
            if dp_left[i] == i or n - dp_right[i] -1 == i:
                continue
            best = min(best, dp_left[i] + dp_right[i])
        return best

    #[2] 1  #how many elements are less than it? 0
    #[1] 2  less than? 0, seen 1, so 1
    #[1] 3 less than? 0, seen 2, so 2 
    #[1,5] less than? 1, seen 3, so 2
    #[1,5,6] less than? 2, seen 4, so 2
    #[1,2,6] less than? 1, seen 5, so 4
    #[1,2,3] less than? 2, seen 6, so 4
    #[1,2,3] 8 less than? 0, seen 7, so 7



        