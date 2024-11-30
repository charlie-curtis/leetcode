class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        ans = 0
        left_cur, right_cur = nums[0], nums[-1]
        i, j = 0, len(nums)-1
        while j > i:
            if left_cur == right_cur:
                i+=1
                j-=1
                left_cur = nums[i]
                right_cur = nums[j]
            elif left_cur > right_cur:
                j-=1
                right_cur+=nums[j]
                ans+=1
            else:
                i+=1
                left_cur+=nums[i]
                ans+=1
        return ans
                

        