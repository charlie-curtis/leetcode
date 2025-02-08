class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        ssum = 0
        T = sum(nums)
        j = 0
        ans = -1
        n = len(nums)
        if T == 0:
            return 0
        if T < x:
            return -1
        if T == x:
            return n
        for i in range(n):
            ssum+=nums[i]
            outside = T - ssum

            while j < i and outside < x:
                ssum-=nums[j]
                outside = T - ssum
                j+=1

            if outside == x:
                ans = max(ans, i-j+1)


        if ans == -1:
            return -1
        return n - ans
            