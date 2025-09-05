class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        mx = max(nums)
        mn = min(nums)
        pos = [0,0]
        for i,x in enumerate(nums):
            if mx == x:
                pos[1] = i
            if mn == x:
                pos[0] = i

        n = len(nums)
        if n == 1:
            return 1
        
        a = max(pos) + 1
        b = n-min(pos)
        c = min(pos) + 1 + n-max(pos)

        return min([a,b,c])
        