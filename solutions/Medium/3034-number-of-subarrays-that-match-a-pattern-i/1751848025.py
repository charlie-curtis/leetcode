class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        n = len(nums)
        k = len(pattern)
        ans = 0
        for i in range(0,n-k):
            good = True
            for j in range(k):
                if pattern[j] == 1:
                    if nums[i+j] >= nums[i+j+1]:
                        good = False
                        break
                elif pattern[j] == -1:
                    if nums[i+j] <= nums[i+j+1]:
                        good = False
                        break
                else:
                    if nums[i+j] != nums[i+j+1]:
                        good = False
                        break
            if good:
                ans+=1
        return ans
                    #pattern = 0