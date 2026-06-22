class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        n = len(nums)
        ans = j = 0
        last = [-1, -1]
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                last = [-1, -1]
                j = i+1
                continue
            
            if nums[i] == minK:
                last[0] = i
            if nums[i] == maxK:
                last[1] = i
            
            if min(last) > -1:
                ans+= min(last) - j + 1
        return ans


        