class Solution:
    def countValidSelections(self, nums: List[int]) -> int:


        total = sum(nums)
        cur = 0
        ans = 0
        n = len(nums)
        for i in range(n):
            cur+=nums[i]
            if nums[i] == 0:
                left = cur
                right = total-cur
                if left == right:
                    ans+=2
                elif abs(left-right) == 1:
                    ans+=1
        return ans