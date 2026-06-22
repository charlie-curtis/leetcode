class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:


        small = []
        large = []

        stale = set()
        j = 0
        ans = 0
        for i,x in enumerate(nums):
            heappush(small, [x, i])
            heappush(large, [-x, i])



            while j < i:
                while small and small[0][1] in stale:
                    heappop(small)
                while large and large[0][1] in stale:
                    heappop(large)
                x,y = small[0][0], abs(large[0][0])
                if abs(x-y) > limit:
                    stale.add(j)
                    j+=1
                else:
                    break
            ans = max(ans, i-j+1)
        return ans