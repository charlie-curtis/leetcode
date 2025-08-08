class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:


        i = 0
        n = len(nums)
        for g in groups:
            L = len(g)
            found = False
            for j in range(i, n-L+1):
                if j+L <= n and g == nums[j:j+L]:
                    found = True
                    i = j+L
                    break
            if not found:
                return False
        return True