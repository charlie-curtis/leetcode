class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:

        nums = nums+nums
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
        
        ans = 10**9 
        for k,v in d.items():
            V = zip(v, v[1:])
            t = 0
            for v1,v2 in zip(v, v[1:]):
                btwn = v2-v1
                half = btwn//2
                t = max(half, t)

            ans = min(ans, t)
        return ans
        