class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        V=set()

        def check(idx):
            if idx in V:
                return 0
            V.add(idx)
            return 1 + check(nums[idx])
        ans=0
        for i in range(len(nums)):
            if i not in V:
                ans=max(ans,check(i))
        return ans