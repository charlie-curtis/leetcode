class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        n = len(nums)
        last_bad = [-1]*n
        for i in range(1,n):
            if nums[i] % 2 == nums[i-1] %2:
                last_bad[i] = i
            else:
                last_bad[i] = last_bad[i-1]

        out = []
        for f,t in queries:
            out.append(last_bad[t] <= f)
        return out

        