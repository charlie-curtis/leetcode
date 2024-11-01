class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:

        m = max(Counter(nums).values())
        n = len(nums)
        for i in range(m):
            #i is the offset
            seen = 0
            for j in range(i,n,m):
                seen+=1
                if j-m >= 0 and nums[j-m] == nums[j]:
                    return False
            if seen < k:
                return False
        return True