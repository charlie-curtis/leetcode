class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:

        def count(t):
            cnt = ans = 0
            for x in nums:
                if x > t:
                    cnt = 0
                else:
                    cnt+=1
                ans+=cnt
            return ans

        return count(r) - count(l-1)


