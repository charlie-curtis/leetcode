class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        ans = 0
        for x in seen:
            if x-1 in seen:
                continue
            
            j = x
            while x in seen:
                x+=1
            ans = max(x-j, ans)
        return ans


            