class Solution:
    def countOfPairs(self, nums: List[int]) -> int:

        n = len(nums)
        M = 10**9 + 7

        #next ele for A has to be >= a1 and next ele for B <= a2
        @cache
        def dp(i, a1, a2):

            if i == n:
                return 1

            ans = 0
            for j in range(nums[i]+1):
                #print(j, nums[i]-j)
                a = nums[i] - j
                b = j
                if a1 > a or a2 < b:
                    break
                t = dp(i+1, a, b) % M
                #print(t)
                ans+=t
                ans%=M
            return ans

        return dp(0, -1e15, 1e15)
        