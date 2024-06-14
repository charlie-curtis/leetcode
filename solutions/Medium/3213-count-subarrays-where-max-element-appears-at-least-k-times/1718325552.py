class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:


        mmax = max(nums)
        locs = deque()
        ans = 0
        for i,x in enumerate(nums):
            if x == mmax:
                locs.append(i)
            if len(locs) > k:
                locs.popleft()
            if len(locs) == k:
                ans+=1 + locs[0]
        return ans